from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Driver, Vehicle
from .serializers import DriverSerializer


class DriverApiTestCase(APITestCase):

    def test_get_post(self):
        driver_1 = Driver.objects.create(first_name='test_name_1', last_name="test_last_name_1")
        driver_2 = Driver.objects.create(first_name='test_name_2', last_name="test_last_name_2")
        url = "http://127.0.0.1:8000/drivers/driver/"
        response = self.client.get(url)
        serializer_data = DriverSerializer([driver_1, driver_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
"""
    def test_driver_detail(self):
        driver_1 = Driver.objects.create(first_name='test_name_1', last_name="test_last_name_1")
        driver_2 = Driver.objects.create(first_name='test_name_2', last_name="test_last_name_2")
        url = "http://127.0.0.1:8000/drivers/driver/<str:id>/"
        response = self.client.get(url)
        serializer_data = DriverSerializer([driver_1, driver_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
"""
