from django.urls import path
from .views import (DriverListAPIView,
                    DriverDetailCRUDAPIView,
                    VehicleListAPIView,
                    VehicleDetailCRUDAPIView,
                    SetVehicleDriverView)

app_name = "park"

urlpatterns = [
    path('driver/', DriverListAPIView.as_view(), name='driver_list'),
    path('driver/<str:id>/', DriverDetailCRUDAPIView.as_view(), name='driver_detail'),
    path('vehicle/', VehicleListAPIView.as_view(), name='vehicle_list'),
    path('vehicle/<str:id>/', VehicleDetailCRUDAPIView.as_view(), name='vehicle_detail'),
    path('set_driver/<int:vehicle_id>/', SetVehicleDriverView.as_view(), name='set_vehicle_driver'),
]