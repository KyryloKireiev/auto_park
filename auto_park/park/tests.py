from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializer


class DriverApiTestCase(APITestCase):
    def test_get_post_driver(self):
        driver_1 = Driver.objects.create(
            first_name="test_name_1", last_name="test_last_name_1"
        )
        driver_2 = Driver.objects.create(
            first_name="test_name_2", last_name="test_last_name_2"
        )
        url = reverse("park:driver_list")
        response = self.client.get(url)
        serializer_data = DriverSerializer([driver_1, driver_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_driver_detail(self):
        driver_1 = Driver.objects.create(
            first_name="test_name_1", last_name="test_last_name_1"
        )
        url = reverse("park:driver_detail", kwargs={"id": driver_1.id})
        response = self.client.get(url)
        serializer_data = DriverSerializer(driver_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_driver_update(self):
        driver_1 = Driver.objects.create(
            first_name="test_name_1", last_name="test_last_name_1"
        )
        driver_1.first_name = "test_name_1_update"
        driver_1.last_name = "test_last_name_1_update"
        driver_1.save()
        url = reverse("park:driver_detail", kwargs={"id": driver_1.id})
        response = self.client.get(url)
        serializer_data = DriverSerializer(driver_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_driver_delete(self):
        driver_1 = Driver.objects.create(
            first_name="test_name_1", last_name="test_last_name_1"
        )
        driver_1.delete()
        url = reverse("park:driver_detail", kwargs={"id": driver_1.id})
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)


class VehicleApiTestCase(APITestCase):
    def test_get_post_vehicle(self):
        vehicle_1 = Vehicle.objects.create(
            make="test_make_1", model="test_model_1", plate_number="test_plate_number_1"
        )
        vehicle_2 = Vehicle.objects.create(
            make="test_make_2", model="test_model_2", plate_number="test_plate_number_2"
        )
        url = reverse("park:vehicle_list")
        response = self.client.get(url)
        serializer_data = VehicleSerializer([vehicle_1, vehicle_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_vehicle_detail(self):
        vehicle_1 = Vehicle.objects.create(
            make="test_make_1", model="test_model_1", plate_number="test_plate_number_1"
        )
        url = reverse("park:vehicle_detail", kwargs={"id": vehicle_1.id})
        response = self.client.get(url)
        serializer_data = VehicleSerializer(vehicle_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_vehicle_update(self):
        vehicle_1 = Vehicle.objects.create(
            make="test_make_1", model="test_model_1", plate_number="test_plate_number_1"
        )
        vehicle_1.make = "test_make_1_update"
        vehicle_1.model = "test_model_1_update"
        vehicle_1.plate_number = "test_plate_number_1_update"
        vehicle_1.save()
        url = reverse("park:vehicle_detail", kwargs={"id": vehicle_1.id})
        response = self.client.get(url)
        serializer_data = VehicleSerializer(vehicle_1).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_vehicle_delete(self):
        vehicle_1 = Vehicle.objects.create(
            make="test_make_1", model="test_model_1", plate_number="test_plate_number_1"
        )
        vehicle_1.delete()
        url = reverse("park:vehicle_detail", kwargs={"id": vehicle_1.id})
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
