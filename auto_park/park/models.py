from django.db import models

#Создаем модель водителя и все ее поля
class Driver(models.Model):

    id = models.BigAutoField(primary_key=True)
    driver_last_name = models.CharField('Фамилия водителя:', max_length=50)
    driver_first_name = models.CharField('Имя водителя:', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.driver_last_name + ' ' + self.driver_first_name

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'

#Создаем модель авто и все ее поля
class Vehicle(models.Model):

    id = models.BigAutoField(primary_key=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle_make = models.CharField('Модель автомобиля:', max_length=50)
    vehicle_model = models.CharField('Марка автомобиля:', max_length=50)
    vehicle_plate_number = models.CharField('Номер автомобиля:', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vehicle_plate_number

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'