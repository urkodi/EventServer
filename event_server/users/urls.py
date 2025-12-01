from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("all", views.get_all_users, name="get all users"),
    path("register", views.create_user, name="Register user"),
    path("login", obtain_auth_token, name="Login user"),
    path("signup", views.SignupView.as_view(), name="Signup user"),
    path("verify", views.VerifyEmailView.as_view(), name="Verify email"),
]