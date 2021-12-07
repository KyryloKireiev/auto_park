from django.urls import path
from .views import DriverListAPIView, \
    DriverDetailCRUDAPIView, VehicleListAPIView, \
    VehicleDetailCRUDAPIView, VehicleCreateDestroyDriverAPIView

app_name = "park"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('driver/', DriverListAPIView.as_view(), name='driver_list'),
    path('driver/<str:id>/', DriverDetailCRUDAPIView.as_view(), name='driver_detail'),
    path('vehicle/', VehicleListAPIView.as_view(), name='vehicle_list'),
    path('vehicle/<str:id>/', VehicleDetailCRUDAPIView.as_view(), name='vehicle_detail'),
    path('set_driver/<str:id>/', VehicleCreateDestroyDriverAPIView.as_view(), name='create_destroy_driver'),
]