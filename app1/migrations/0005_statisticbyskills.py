# Generated by Django 4.1.5 on 2023-01-23 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_statisticbycity_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatisticBySkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Наавык')),
                ('number_of_references', models.IntegerField(verbose_name='Количество упоминаний')),
            ],
        ),
    ]
