from django.http import JsonResponse
from .models import TopSkills
from django.http import HttpRequest

def get_top_skills(request: HttpRequest, title, year):
    data = TopSkills.objects.filter(year=year, title=title).values('image', 'table')
    print(data)
    return JsonResponse(list(data), safe=False)