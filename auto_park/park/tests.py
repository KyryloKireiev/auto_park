from django.core.exceptions import ObjectDoesNotExist
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
        driver = Driver.objects.create(
            first_name="test_name_1", last_name="test_last_name_1"
        )
        url = reverse("park:driver_detail", kwargs={"id": driver.id})
        response = self.client.get(url)
        serializer_data = DriverSerializer(driver).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_driver_update(self):
        driver = Driver.objects.create(
            first_name="test_name_1", last_name="test_last_name_1"
        )
        updated_first_name = "test_name_1_update"
        updated_last_name = "test_last_name_1_update"

        url = reverse("park:driver_detail", kwargs={"id": driver.id})
        response = self.client.patch(
            url,
            data={
                "first_name": updated_first_name,
                "last_name": updated_last_name,
            },
        )

        driver = Driver.objects.get(pk=driver.id)
        serializer_data = DriverSerializer(driver).data

        self.assertEqual(driver.first_name, updated_first_name)
        self.assertEqual(driver.last_name, updated_last_name)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_driver_delete(self):
        driver = Driver.objects.create(
            first_name="test_name_1", last_name="test_last_name_1"
        )
        url = reverse("park:driver_detail", kwargs={"id": driver.id})
        response = self.client.delete(url)
        self.assertRaises(ObjectDoesNotExist, Driver.objects.get, pk=driver.id)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)


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
        vehicle = Vehicle.objects.create(
            make="test_make_1", model="test_model_1", plate_number="test_plate_number_1"
        )
        url = reverse("park:vehicle_detail", kwargs={"id": vehicle.id})
        response = self.client.get(url)
        serializer_data = VehicleSerializer(vehicle).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_vehicle_update(self):
        vehicle = Vehicle.objects.create(
            make="test_make_1", model="test_model_1", plate_number="test_plate_number_1"
        )
        updated_make = "test_name_1_update"
        updated_model = "test_last_name_1_update"
        updated_plate_number = "test_plate_number_1_update"
        url = reverse("park:vehicle_detail", kwargs={"id": vehicle.id})
        response = self.client.patch(
            url,
            data={
                "make": updated_make,
                "model": updated_model,
                "plate_number": updated_plate_number,
            },
        )
        vehicle = Vehicle.objects.get(pk=vehicle.id)
        serializer_data = VehicleSerializer(vehicle).data
        self.assertEqual(vehicle.make, updated_make)
        self.assertEqual(vehicle.model, updated_model)
        self.assertEqual(vehicle.plate_number, updated_plate_number)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_vehicle_delete(self):
        vehicle_1 = Vehicle.objects.create(
            make="test_make_1", model="test_model_1", plate_number="test_plate_number_1"
        )
        url = reverse("park:vehicle_detail", kwargs={"id": vehicle_1.id})
        response = self.client.delete(url)
        self.assertRaises(ObjectDoesNotExist, Vehicle.objects.get, pk=vehicle_1.id)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
