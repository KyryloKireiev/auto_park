from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Driver
from .serializers import DriverSerializer

class DriverView(APIView):
    def get(self, request):
        drivers = Driver.objects.all()
        # the many param informs the serializer that it will be serializing more than a single driver.
        serializer = DriverSerializer(drivers, many=True)
        return Response({"drivers": serializer.data})

    def post(self, request):
        driver = request.data.get('driver')
        # Create a driver from the above data
        serializer = DriverSerializer(data=driver)
        if serializer.is_valid(raise_exception=True):
            driver_saved = serializer.save()
        return Response({"success": "Driver '{}' created successfully".format(driver_saved.title)})



