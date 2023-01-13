from django.shortcuts import render
from jinja2 import Environment, FileSystemLoader
from app1.models import StatisticByYear, StatisticByCity
from app1.hh import get_vacancies, get_last_vacancies

def index_page(request):
    return render(request, 'index.html')


def geography_page(request):
    data = {
        'statistics_by_cities': StatisticByCity.objects.get_queryset(),
    }
    return render(request, 'geography.html', context=data)


def skills_page(request):
    return render(request, 'skills.html')


def last_vacancies_page(request, vacancy_count=10):
    vacancies = get_last_vacancies(n=vacancy_count)
    data = {
        'vacancies': vacancies,
        'pairwise': lambda iterable: zip(iter(iterable), iter(iterable))
    }
    return render(request, 'last_vacancies.html', context=data)


def demand_page(request):
    data = {
        'statistics_by_years': StatisticByYear.objects.get_queryset(),
        'name': 'DevOps'
    }
    return render(request, 'demand.html', context=data)
