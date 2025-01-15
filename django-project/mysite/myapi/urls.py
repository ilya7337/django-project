from django.urls import path
from .views import get_last_vac, get_top_skills


name = 'myapi'

urlpatterns = [
    path('last_vac/', get_last_vac, name='get_last_vac'),
    path('top_skills/<str:title>/<int:year>/', get_top_skills, name='get_top_general_skills'),
]


