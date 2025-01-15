from django.http import JsonResponse
from backDev.models import TopSkills
from django.http import HttpRequest
import asyncio
from .last_vac import last_vac


def get_top_skills(request: HttpRequest, title, year):
    data = TopSkills.objects.filter(year=year, title=title).values('image', 'table')
    return JsonResponse(list(data), safe=False)


def get_last_vac(request):
    """Возвращает список словарей с последними 10 вакансиями"""
    res = asyncio.run(last_vac())
    res = sorted(res.values(), key=lambda vac: vac['published_at'][:-1], reverse=True)[:10]
    return JsonResponse(res, safe=False)

