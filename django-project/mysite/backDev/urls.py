from django.urls import path
from .views import get_article, main_article, get_last_vac_view, page_not_found
from .last_vac import get_last_vac
from .top_skills import get_top_skills
from django.conf.urls import handler404

name = 'backDev'

urlpatterns = [
    path('', main_article, name='main'),
    path('last_vac/', get_last_vac_view, name='get_last_vac_view'),
    path('api/last_vac/', get_last_vac, name='get_last_vac'),
    path('api/top_skills/<str:title>/<int:year>/', get_top_skills, name='get_top_general_skills'),
    path('<slug:slug>/', get_article, name='get_article'),
]


handler404 = page_not_found