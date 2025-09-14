from django.shortcuts import render, redirect, get_object_or_404
from main.forms import Itemsform
from main.models import Item
# Create your views here.
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