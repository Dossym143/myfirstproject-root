from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('Это новая страница')


def home(request):
    return render(request, 'home.html', {'greeting': 'Salam!'})