from django.shortcuts import render
from django.http import HttpResponse
from .models import User
 
import json
import bcrypt

def index(request):
    return HttpResponse("Hello")

def get_all_users(request):
    users = User.objects.all()
    return HttpResponse(users)

def create_user(request):
    """
    POST /register

    Request Body:
     - firstName: str
     - lastName: str
     - password: str
     - email: str
    """
    if request.method == "POST":
        body =  request.body.decode("utf-8")
        body = json.loads(body)

        first_name = body["firstName"]
        last_name = body["lastName"]
        email = body["email"]
        password = body["password"]

        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        new_user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password_hash = hashed_password, pfp_path = None)
        new_user.save()

        return HttpResponse(new_user)

    return HttpResponse("What are you even doing bruv.")



