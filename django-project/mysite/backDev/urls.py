from django.urls import path
from .views import get_article, main_article, get_last_vac_view
from .last_vac import get_last_vac

name = 'backDev'

urlpatterns = [
    path('', main_article, name='main'),
    path('last_vac/', get_last_vac_view, name='get_last_vac_view'),
    path('api/last_vac/', get_last_vac, name='get_last_vac'),
    path('<slug:slug>/', get_article, name='get_article'),
]
