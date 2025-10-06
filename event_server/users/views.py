from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def index(request):
    return HttpResponse("Hello")

def get_all_users(request):
    users = User.objects.all()
    return HttpResponse(users)