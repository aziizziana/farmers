from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Farmer, District, SubCounty, Officer, Harvest, Report

# Register your models here.
admin.site.register(Farmer)
admin.site.register(District)
admin.site.register(SubCounty)
admin.site.register(Officer)
admin.site.register(Report)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Harvest)