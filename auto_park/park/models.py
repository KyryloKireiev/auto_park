from django.db import models

# Create your models here.

class Driver(models.Model):

    driver_last_name = models.CharField('Фамилия водителя:', max_length=50)
    driver_first_name = models.CharField('Имя водителя:', max_length=50)
    drive_date = models.DateTimeField('Время приезда в автопарк:')

    def __str__(self):
        return self.driver_last_name + ' ' + self.driver_first_name

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'

class Vehicle(models.Model):

    vehicle_make = models.CharField('Год выпуска автомобиля:', max_length=50)
    vehicle_model = models.CharField('Модель автомобиля:', max_length=50)
    vehicle_plate_number = models.CharField('Номер автомобиля:', max_length=50)

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_plate_number

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'