from django.shortcuts import render
from .forms import ArticleForm
from django.http import HttpRequest, HttpResponse
from .models import Article


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


def get_last_vac_view(request: HttpRequest):
    nav = Article.objects.values('title', 'slug')
    return render(request, 'backDev/last_vac.html', {'nav': nav})





