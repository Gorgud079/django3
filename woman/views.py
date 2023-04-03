from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from woman import constanta
from .models import Woman, Category

def index(request):
    post = Woman.objects.all()
    context = {
        'post': post,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'woman/index.html', context=context)

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

def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('<h1>Обратная связь</h1>')

def login(request):
    return HttpResponse('Авторизация')

def show_page(request, post_id):
    return HttpResponse(f"Отображение статьи {post_id}")

def show_category(request, cat_id):
    post = Woman.objects.filter(cat_id=cat_id)
    context = {
        'post': post,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'woman/index.html', context=context)