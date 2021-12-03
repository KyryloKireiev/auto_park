from django.contrib import admin
from .models import Driver, Vehicle
#Регистрируем модели водителя и авто в админке
admin.site.register(Driver)
admin.site.register(Vehicle)


