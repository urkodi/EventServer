from django.urls import path
from . import views

urlpatterns = [
    path("reverse-geocode", views.reverse_geocode, name="get and address from a latitude and longitude"),
]