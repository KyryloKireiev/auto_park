from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Driver, Vehicle
from .serializers import DriverSerializer, DriverDetailCRUDSerializer, VehicleSerializers, VehicleDetailCRUDSerializer

#Класс: просмотр списка водителей и создание нового водителя
class DriverListAPIView(ListCreateAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()

#Класс: просмотр информации по водителю, редактирование и удаление водителя по ID
class DriverDetailCRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DriverDetailCRUDSerializer
    queryset = Driver.objects.all()
    lookup_field = 'id'

#Класс: просмотр списка автомобилей и создание нового автомобиля
class VehicleListAPIView(ListCreateAPIView):
    serializer_class = VehicleSerializers
    queryset = Vehicle.objects.all()

#Класс: просмотр информации по автомобилю, редактирование и удаление автомобиля по ID

class VehicleDetailCRUDAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleDetailCRUDSerializer
    queryset = Vehicle.objects.all()
    lookup_field = 'id'
