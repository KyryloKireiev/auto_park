from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Driver
from .serializers import DriverSerializer, DriverDetailSerializer

#Класс создание нового водителя
class DriverListAPIView(ListCreateAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

#Класс просмотра, редактирования и удаления водителя по ID
class DriverDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DriverDetailSerializer
    queryset = Driver.objects.all()
    lookup_field = 'id'
