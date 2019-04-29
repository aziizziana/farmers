from django.urls import path

from . import views
from accounts.api import FarmerApi, FarmerDeleteApi


urlpatterns = [
        path('farmers', FarmerApi.as_view()),
        path('farmers/<int:pk>', FarmerDeleteApi.as_view())
       
]
