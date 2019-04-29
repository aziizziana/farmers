from django.db import models

# Create your models here.
class Farmer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    district_id = models.ForeignKey('District', on_delete=models.CASCADE)
    subcounty_id = models.ForeignKey('SubCounty', on_delete=models.CASCADE)
    parish = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    birth_year = models.CharField(max_length=200)
    marriage = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    photo= models.ImageField(upload_to='images')
    community_status = models.CharField(max_length=200)
    instructor_possibility = models.BooleanField()
    farm_area = models.CharField(max_length=200)
    crop_type = models.CharField(max_length=200)
    past_harvests = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)

    def __repr__(self):
        return f"Farmer('{self.first_name}', '{self.last_name}')"


class District(models.Model):
    name = models.CharField(max_length=200, default='KAMPALA')

class SubCounty(models.Model):
    name = models.CharField(max_length=200, default='MENGO')
    
class Harvest(models.Model):
    season_id = models.ForeignKey('Season', on_delete=models.CASCADE)
    area = models.CharField(max_length=200)
    harvest = models.CharField(max_length=200)

class Season(models.Model):
    name = models.CharField(max_length=200)

class Report(models.Model):
    season_id = models.ForeignKey('Season', on_delete=models.CASCADE)
    farm_area = models.CharField(max_length=200)
    rice_type = models.CharField(max_length=200)
    sowing_date = models.DateTimeField()
    sowing_type = models.CharField(max_length=200)
    planting_type = models.CharField(max_length=200)
    levelling = models.CharField(max_length=200)
    ridge = models.CharField(max_length=200)
    watercourse_state = models.CharField(max_length=200)
    fertilizer = models.BooleanField()
    fertilizer_1_type = models.CharField(max_length=200)
    fertilizer_1_amount = models.CharField(max_length=200)
    fertilizer_2_type = models.CharField(max_length=200)
    fertilizer_2_amount = models.CharField(max_length=200)
    weed_condition = models.CharField(max_length=200)
    total_weed_times = models.CharField(max_length=200)
    harvest_date = models.DateTimeField()
    harvest_amount = models.CharField(max_length=200)
    note = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images')



class Officer(models.Model):
    name = models.CharField(max_length=200)
    login_id = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    district_id = models.ForeignKey('District', on_delete=models.CASCADE)
    subcounty_id = models.ForeignKey('SubCounty', on_delete=models.CASCADE)
    phone = models.CharField(max_length=200)


  