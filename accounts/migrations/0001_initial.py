# Generated by Django 2.2 on 2019-04-17 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='KAMPALA', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubCounty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='MENGO', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_area', models.CharField(max_length=200)),
                ('rice_type', models.CharField(max_length=200)),
                ('sowing_date', models.DateTimeField()),
                ('sowing_type', models.CharField(max_length=200)),
                ('planting_type', models.CharField(max_length=200)),
                ('levelling', models.CharField(max_length=200)),
                ('ridge', models.CharField(max_length=200)),
                ('watercourse_state', models.CharField(max_length=200)),
                ('fertilizer', models.BooleanField()),
                ('fertilizer_1_type', models.CharField(max_length=200)),
                ('fertilizer_1_amount', models.CharField(max_length=200)),
                ('fertilizer_2_type', models.CharField(max_length=200)),
                ('fertilizer_2_amount', models.CharField(max_length=200)),
                ('weed_condition', models.CharField(max_length=200)),
                ('total_weed_times', models.CharField(max_length=200)),
                ('harvest_date', models.DateTimeField()),
                ('harvest_amount', models.CharField(max_length=200)),
                ('note', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='images')),
                ('season_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Season')),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('login_id', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.District')),
                ('subcounty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.SubCounty')),
            ],
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=200)),
                ('harvest', models.CharField(max_length=200)),
                ('season_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Season')),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('parish', models.CharField(max_length=200)),
                ('village', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('birth_year', models.CharField(max_length=200)),
                ('marriage', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='images')),
                ('community_status', models.CharField(max_length=200)),
                ('instructor_possibility', models.BooleanField()),
                ('farm_area', models.CharField(max_length=200)),
                ('crop_type', models.CharField(max_length=200)),
                ('past_harvests', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.District')),
                ('subcounty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.SubCounty')),
            ],
        ),
    ]
