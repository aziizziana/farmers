# Generated by Django 2.2 on 2019-04-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190413_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='district',
            field=models.CharField(default='KAMPALA', max_length=200),
        ),
        migrations.AlterField(
            model_name='subcounty',
            name='subcounty',
            field=models.CharField(default='MENGO', max_length=200),
        ),
    ]