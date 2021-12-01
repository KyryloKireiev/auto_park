from django.urls import path
from .views import DriverView

app_name = "park"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('driver/', DriverView.as_view()),
]