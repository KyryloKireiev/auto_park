from rest_framework import serializers
from .models import Driver, Vehicle

# удалить 2 сериалайзера!!!

#Создаем сериалайзер, который возвращает список фамилий водителей
# и позволяет создать нового водителя GET and POST
class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = '__all__'

#Создаем сериалайзер, который возвращает детальную инфу о водителе и позволяет
# редактировать и удалять водителя GET, UPDATE, DELETE
class DriverDetailCRUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = '__all__'

#Создаем сериалайзер, который возвращает список автомобилей
# и позволяет создать нового водителя GET and POST

class VehicleSerializers(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'

#Создаем сериалайзер, который возвращает детальную инфу об автомобиле и позволяет
# редактировать и удалять автомобиль GET, UPDATE, DELETE

class VehicleDetailCRUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = '__all__'


