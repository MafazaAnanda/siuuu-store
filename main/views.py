from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import datetime
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import Itemsform
from main.models import Item

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    category = request.GET.get("category")
    if (filter_type == "all"):
        item_list = Item.objects.all()
    else:
        item_list = Item.objects.filter(user=request.user)
    if category:
        item_list = item_list.filter(category=category)

    context = {
        'store_name' : 'siuuu-store',
        'name': request.user.username,
        'npm' : '2406401306',
        'item_list' : item_list,
        'last_login' : request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def add_item(request):
    form = Itemsform(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item_entry = form.save(commit=False)
        item_entry.user  = request.user
        item_entry.save()
        return redirect ('main:show_main')
    
    context = {'form': form}
    return render(request, 'add_item.html', context)

@login_required(login_url='/login')
def show_item(request, id):
    item = get_object_or_404(Item, pk=id)

    context = {
        'item': item
    }

    return render(request, "item_detail.html", context)

def show_xml(request):
    item_list = Item.objects.all()
    xml_data = serializers.serialize("xml", item_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    item_list = Item.objects.all()
    data = [
        {
            'id': str(item.id),
            'name': item.name,
            'description': item.description,
            'category': item.category,
            'thumbnail': item.thumbnail,
            'is_featured': item.is_featured,
            'stock' : item.stock,
            'brand' : item.brand,
            'user_id': item.user_id,
            'price' : item.price,
        }
        for item in item_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, item_id):
    try:
        item = Item.objects.filter(pk=item_id)
        xml_data = serializers.serialize("xml", item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Item.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, item_id):
    try:
        item = Item.objects.select_related('user').get(pk=item_id)
        data = {
            'id': str(item.id),
            'name': item.name,
            'description': item.description,
            'category': item.category,
            'thumbnail': item.thumbnail,
            'is_featured': item.is_featured,
            'stock' : item.stock,
            'brand' : item.brand,
            'user_id': item.user_id,
            'user_username': item.user.username if item.user_id else None,
            'is_trusted': item.user.is_authenticated if item.user else False,
        }
        return JsonResponse(data)
    except Item.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        
    context = {'form' : form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        
    else:
        form = AuthenticationForm(request)

    context = {'form' : form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_item(request, id):
    item = get_object_or_404(Item, pk=id)
    form = Itemsform(request.POST or None, instance=item)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_item.html", context)

@require_POST
def delete_item(request, id):
    try:
        item = get_object_or_404(Item, pk=id)
        if item.user == request.user:
            item.delete()
            return JsonResponse({'status': 'success', 'message': 'Item berhasil dihapus.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Anda tidak punya izin untuk menghapus item ini.'}, status=403)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
@csrf_exempt
@require_POST
def add_item_entry_ajax(request):
    name = strip_tags(request.POST.get("name"))
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    price = request.POST.get("price")
    stock = request.POST.get("stock")
    brand = request.POST.get("brand")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_item = Item(
        name=name, 
        description=description,
        category=category,
        thumbnail=thumbnail,
        price=price,
        stock=stock,
        brand=brand,
        is_featured=is_featured,
        user=user

    )
    new_item.save()

    return HttpResponse(b"CREATED", status=201)

@login_required
@csrf_exempt 
def edit_item_ajax(request, id):
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=id)

        if item.user != request.user:
            return JsonResponse({"status": "error", "message": "You do not have permission to edit this item."}, status=403)

        item.name = request.POST.get("name")
        item.price = int(request.POST.get("price"))
        item.description = request.POST.get("description")
        item.thumbnail = request.POST.get("thumbnail")
        item.category = request.POST.get("category")
        item.stock = int(request.POST.get("stock"))
        item.brand = request.POST.get("brand")
        item.is_featured = request.POST.get("is_featured") == 'on'
        
        item.save()

        return JsonResponse({"status": "success"})
    
    return JsonResponse({"status": "error"}, status=400)

@login_required
def get_item_json(request, id):
    """
    View to get a single item data in JSON format.
    """
    item = get_object_or_404(Item, pk=id)
    if item.user != request.user:
        return JsonResponse({"status": "error", "message": "Unauthorized"}, status=403)
        
    return HttpResponse(serializers.serialize('json', [item]), content_type="application/json")