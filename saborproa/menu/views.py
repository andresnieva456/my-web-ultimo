from django.shortcuts import render

def index(request):
    return render(request, 'menu/index.html')

def desayunos(request):
    return render(request, 'menu/desayunos.html')

def almuerzos(request):
    return render(request, 'menu/almuerzos.html')

def cenas(request):
    return render(request, 'menu/cenas.html')

