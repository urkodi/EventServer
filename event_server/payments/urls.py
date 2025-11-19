from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('create-checkout-session', views.create_checkout_session, name='create_checkout_session'),
]