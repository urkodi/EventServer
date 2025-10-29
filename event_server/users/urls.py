from django.urls import path
from . import views

urlpatterns = [
    path("all", views.get_all_users, name="get all users"),
    path("register", views.create_user, name="Register user"),
    path("login", views.login_user, name="Login user")
]