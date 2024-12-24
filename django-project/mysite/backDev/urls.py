from django.urls import path
from .views import get_article, main_article, get_last_vac_v

name = 'backDev'

urlpatterns = [
    path('', main_article, name='main'),
    path('last_vac/', get_last_vac_v, name='get_last_vac'),
    path('<slug:slug>/', get_article, name='get_article'),
]
