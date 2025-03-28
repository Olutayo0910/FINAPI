from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CBNData
from .serializers import CBNDataserializer

class CBNDataViewSet(viewsets.ModelViewSet):
    queryset = CBNData.objects.all()
    serializer_class = CBNDataserializer
