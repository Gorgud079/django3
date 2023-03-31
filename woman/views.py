from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from woman import constanta
from .models import Woman

def index(request):
    post = Woman.objects.all()
    return render(request, 'woman/index.html', {'post': post, 'menu': constanta.menu, 'title': 'Главная'})

def about(request):
    return render(request, 'woman/about.html', {'menu': constanta.menu, 'title': 'О нас'})

def categories(request, cat):
    print(request.GET)
    return HttpResponse(f'<h1>Страница приложения!!! </h1><p>{cat}</p>')

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)
    return HttpResponse(f'<h1>Архив по годам! </h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!!</h1>')