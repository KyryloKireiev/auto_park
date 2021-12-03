from rest_framework import serializers
from .models import Driver

#Создаем сериалайзер, который возвращает список фамилий водителей
# и позволяет создать нового водителя GET and POST
class DriverSerializer(serializers.ModelSerializer):

    driver_first_name = serializers.CharField(write_only=True, max_length=50)
    driver_last_name = serializers.CharField(max_length=50)

    class Meta:
        model = Driver
        fields = [
            'driver_first_name', 'driver_last_name'
        ]

#Создаем сериалайзер, который возвращает детальную инфу о водителе и позволяет
# редактировать и удалять водителя GET, UPDATE, DELETE
class DriverDetailSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    driver_first_name = serializers.CharField(max_length=50)
    driver_last_name = serializers.CharField(max_length=50)
    created_at = serializers.DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")
    updated_at = serializers.DateTimeField(read_only=True, format="%d/%m/%Y %H:%M:%S")

    class Meta:
        model = Driver
        fields = '__all__'



