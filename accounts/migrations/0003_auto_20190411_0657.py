# Generated by Django 2.2 on 2019-04-11 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_harvest_officer_report_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='harvest_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='report',
            name='sowing_date',
            field=models.DateTimeField(),
        ),
    ]
