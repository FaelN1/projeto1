from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', {
        'name': 'Rafael'
    })


def contato(request):
    return render(request, 'temp.html')


def sobre(request):
    return HttpResponse('sobre')
