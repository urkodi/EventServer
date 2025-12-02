from django.urls import path
from . import views

urlpatterns = [
    path("create", views.create_event, name="create an event"),
    path("list_all",views.list_events, name="list all events"),
    path("list_all_by_owner", views.list_events_by_owner, name="list events by id"),
]
