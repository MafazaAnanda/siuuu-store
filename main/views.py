from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import Itemsform
from main.models import Item

def show_main(request):
    item_list = Item.objects.all()
    context = {
        'store_name' : 'siuuu-store',
        'name': 'Mafaza Ananda Rahman',
        'npm' : '2406401306',
        'item_list' : item_list
    }

    return render(request, "main.html", context)

def add_item(request):
    form = Itemsform(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect ('main:show_main')
    
    context = {'form': form}
    return render(request, 'add_item.html', context)

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
    json_data = serializers.serialize("json", item_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, item_id):
    try:
        item = Item.objects.filter(pk=item_id)
        xml_data = serializers.serialize("xml", item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Item.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, item_id):
    try:
        item = Item.objects.filter(pk=item_id)
        json_data = serializers.serialize("json", item)
        return HttpResponse(json_data, content_type="application/json")
    except Item.DoesNotExist:
        return HttpResponse(status=404)
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been succesfully created!')
            return redirect('main:login')
        
    context = {'form' : form}
    return render(request, 'register.html', context)