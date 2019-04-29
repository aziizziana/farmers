from django.urls import path

from . import views
from accounts.api import FarmerApi


urlpatterns = [
        path('farmers', FarmerApi.as_view())
       
]
