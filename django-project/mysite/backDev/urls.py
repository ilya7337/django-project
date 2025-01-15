from django.urls import path
from .views import get_article, main_article, get_last_vac_view, page_not_found

from django.conf.urls import handler404

name = 'backDev'

urlpatterns = [
    path('', main_article, name='main'),
    path('last_vac/', get_last_vac_view, name='get_last_vac_view'),
    
    path('<slug:slug>/', get_article, name='get_article'),
]


handler404 = page_not_found