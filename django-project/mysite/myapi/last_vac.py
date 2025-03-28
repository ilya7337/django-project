import asyncio
import aiohttp
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


def get_salary(salary):
    if salary is None:
        return "Доход не указан"
    else:
        if salary['from'] is None and salary['to'] is not None:
            return f"До {salary['to']} {salary['currency']}"
        elif salary['from'] is not None and salary['to'] is None:
            return f"От {salary['from']} {salary['currency']}"
        else:
            return f"От {salary['from']} до {salary['to']} {salary['currency']}"


def clean_html(html_text):
    """Удаляет html теги"""
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup.get_text()


def get_skills(skills):
    """Достает вакансии и превращает в строку"""
    if not skills:
        return "Навыки не указаны"
    return ", ".join(skill['name'] for skill in skills)


async def get_desc_sk(url, session):
    """Делает доп. запрос для получения описания и скилов по вакансии"""
    async with session.get(url) as response:
        if response.status == 200:
            vacancies = await response.json()
        else:
            return '', ''
    description = clean_html(vacancies.get('description', 'Нет описания'))
    skills = get_skills(vacancies.get('key_skills', []))
    return description, skills


async def get_vacancies(profession, session, result, lock):
    """Получает вакансиями по заданной профессии"""
    params = {
        'text': profession,
        'period': 1,
        'per_page': 10,
        "search_field": 'name',
        'page': 0,
        'order_by': 'publication_time'
    }
    
    async with session.get('https://api.hh.ru/vacancies', params=params) as response:
        if response.status == 200:
            vacancies = await response.json()
        else:
            return

    if not vacancies:
        return

    for vacancy in vacancies.get('items', []):
        if vacancy['id'] in result:
            continue
        vacancy_data = {
            'id': vacancy['id'],
            'title': vacancy['name'],
            'company': vacancy['employer']['name'],
            'salary': get_salary(vacancy['salary']),
            'region': vacancy['area']['name'],
            'published_at': vacancy['published_at'][:10],
            'description': '',
            'skills': ''
        }
        vacancy_data['description'], vacancy_data['skills'] = await get_desc_sk(vacancy['url'], session)
        async with lock:
            result[vacancy['id']] = vacancy_data


async def last_vac():
    """Возвращает список словарей с последними вакансиями"""
    result = {}
    lock = asyncio.Lock()
    profession_variants = [
        'backend', 'бэкэнд', 'бэкенд', 'бекенд', 'бекэнд',
        'back end', 'бэк энд', 'бэк енд', 'django', 'flask',
        'laravel', 'yii', 'symfony'
    ]

    async with aiohttp.ClientSession(trust_env=True) as session:
        tasks = [get_vacancies(profession, session, result, lock) for profession in profession_variants]
        await asyncio.gather(*tasks)
    return result


