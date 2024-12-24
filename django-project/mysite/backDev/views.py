from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from django.http import HttpRequest, HttpResponse
from .models import Article
from .last_vac import get_last_vac

def main_article(request: HttpRequest):
    nav = Article.objects.values('title', 'slug')
    try:
        article = Article.objects.get(title='Главная страница')
    except Article.DoesNotExist:
        return render(request, 'backDev/article.html', {'error': 'Статья не найдена.', 'nav': nav})
    
    return render(request, 'backDev/article.html', {'article': article, 'nav': nav})


def get_article(request: HttpRequest, slug):
    nav = Article.objects.values('title', 'slug')
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return render(request, 'backDev/article.html', {'error': 'Статья не найдена', 'nav': nav})
    
    return render(request, 'backDev/article.html', {'article': article, 'nav': nav})


def get_last_vac_v(request: HttpRequest):
    vacancies = get_last_vac()
    nav = Article.objects.values('title', 'slug')
    return render(request, 'backDev/last_vac.html', {'vacancies': vacancies, 'nav': nav})





