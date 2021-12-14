from django.db import models


class Driver(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField("First name:", max_length=50)
    last_name = models.CharField("Last name:", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"


class Vehicle(models.Model):
    id = models.BigAutoField(primary_key=True)
    driver = models.OneToOneField(
        Driver, on_delete=models.SET_NULL, blank=True, null=True,
    )
    make = models.CharField("Make:", max_length=50)
    model = models.CharField("Model:", max_length=50)
    plate_number = models.CharField("Plate number:", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plate_number

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"
