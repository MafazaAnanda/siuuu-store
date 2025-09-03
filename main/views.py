from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406401306',
        'name': 'Mafaza Ananda Rahman',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)