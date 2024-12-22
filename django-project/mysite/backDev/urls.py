from django.urls import path
from .views import create_article, get_all_articles

name = 'backDev'

urlpatterns = [
    path('create/', create_article, name='create_article'),
    path('articles/', get_all_articles, name='all_articles'),
]
