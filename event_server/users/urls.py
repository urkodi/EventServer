from django.urls import path
from . import views

urlpatterns = [
    path("all", views.get_all_users, name="get_all_users"),
    path("register", views.create_user, name="register_user"),
    path("login", views.login_user, name="login_user"),
    path("user_details", views.get_user_by_id, name="get_user_by_id"),
    path("update_user", views.update_user, name="update_user"),
    path("logged_in", views.get_logged_in_user, name="logged_in_user"),
    path("signup", views.SignupView.as_view(), name="Signup user"),
    path("verify", views.VerifyEmailView.as_view(), name="Verify email"),
]
