# Generated by Django 2.2 on 2019-04-10 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_area', models.CharField(max_length=200)),
                ('rice_type', models.CharField(max_length=200)),
                ('sowing_date', models.CharField(max_length=200)),
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
                ('harvest_date', models.CharField(max_length=200)),
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
    ]