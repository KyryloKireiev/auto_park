from django.urls import path
from .views import DriverListAPIView, DriverDetailAPIView

app_name = "park"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('driver/', DriverListAPIView.as_view()),
    path('driver/<str:id>/', DriverDetailAPIView.as_view(), name='driver_detail'),
]