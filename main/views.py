from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'store_name' : 'siuuu-store',
        'name': 'Mafaza Ananda Rahman',
        'npm' : '2406401306'
    }

    return render(request, "main.html", context)