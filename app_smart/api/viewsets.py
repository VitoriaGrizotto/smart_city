from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response 
from rest_framework import viewsets
from app_smart.api import serializers
from app_smart.models import Sensor, TemperaturaData
from app_smart.api.serializers import TemperaturaDataSerializer, UmidadeDataSerializer, LuminosidadeDataSerializer, ContadorDataSerializer
# from app_smart.api.viewsets import TemperaturaDataViewSet
from django_filters.rest_framework import DjangoFilterBackend
from app_smart.api.filters import SensorFilter
from app_smart.api.filters import TemperaturaDataFilter
from app_smart.models import TemperaturaData, UmidadeData, LuminosidadeData, ContadorData
import csv


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = serializers.SensorSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SensorFilter

    
class TemperaturaDataViewSet(viewsets.ModelViewSet):
    queryset = TemperaturaData.objects.all()
    serializer_class = serializers.TemperaturaDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = TemperaturaDataFilter

class TemperatureDataList(generics.ListAPIView):
    queryset = TemperaturaData.objects.all()
    serializer_class = TemperaturaDataSerializer

class UmidadeDataViewSet(viewsets.ModelViewSet):    
    queryset = UmidadeData.objects.all()
    serializer_class = serializers.UmidadeDataSerializer    
   
 
class UmidadeDataList(generics.ListAPIView):
    queryset = UmidadeData.objects.all()
    serializer_class = UmidadeDataSerializer
 
 
class ContadorDataViewSet(viewsets.ModelViewSet):    
    queryset = ContadorData.objects.all()
    serializer_class = serializers.ContadorDataSerializer    
   
 
class ContadorDataList(generics.ListAPIView):
    queryset = ContadorData.objects.all()
    serializer_class = ContadorDataSerializer
 
class LuminosidadeDataViewSet(viewsets.ModelViewSet):    
    queryset = LuminosidadeData.objects.all()
    serializer_class = serializers.LuminosidadeDataSerializer    
   
 
class LuminosidadeDataList(generics.ListAPIView):
    queryset = LuminosidadeData.objects.all()
    serializer_class = LuminosidadeDataSerializer

