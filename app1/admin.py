from django.contrib import admin
from app1.models import Profession, StatisticByYear, StatisticByCity, StatisticBySkills

admin.site.register(Profession)
admin.site.register(StatisticByYear)
admin.site.register(StatisticByCity)
admin.site.register(StatisticBySkills)
