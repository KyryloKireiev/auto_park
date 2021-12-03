from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Driver
from .serializers import DriverSerializer, DriverDetailSerializer

#Класс: создание нового водителя и просмотр списка водителей
class DriverListAPIView(ListCreateAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

#Класс: просмотр, редактирование и удаление водителя по ID
class DriverDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DriverDetailSerializer
    queryset = Driver.objects.all()
    lookup_field = 'id'
