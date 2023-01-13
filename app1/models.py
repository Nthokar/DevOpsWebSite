from django.db import models


class Profession(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')


class StatisticByYear(models.Model):
    title = models.CharField('Год', max_length=4)

    average_salary = models.FloatField('Средняя зарплата')
    average_salary_for_name = models.FloatField('Средняя зарплата - DevOps')
    vacancies_count = models.IntegerField('Количество вакансий')
    vacancies_count_for_name = models.IntegerField('Количество вакансий - DevOps')


class StatisticByCity(models.Model):
    title = models.CharField('Город', max_length=20)

    average_salary = models.FloatField('Уровень зарплат по городам')
    proportion = models.FloatField('Доля вакансий по городам')
