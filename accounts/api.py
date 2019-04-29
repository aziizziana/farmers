from accounts.models import Farmer
from rest_framework import viewsets, permissions
from .serializers import FarmerSerializer
from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView)

class FarmerApi(ListAPIView, CreateAPIView):
    serializer_class = FarmerSerializer
    queryset = Farmer.objects.all()

class FarmerDeleteApi(RetrieveUpdateDestroyAPIView):
    serializer_class = FarmerSerializer
    queryset = Farmer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FarmerSerializer