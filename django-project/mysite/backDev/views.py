from django.shortcuts import render, redirect
from .forms import ArticleForm
from django.http import HttpRequest, HttpResponse
from .models import Article

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ArticleForm()
    return render(request, 'backDev/create_article.html', {'form': form})



def get_all_articles(request: HttpRequest):
    articles = Article.objects.all()
    return render(request, 'backDev/all_article.html', {'articles': articles})