from django.shortcuts import render
from django.http import HttpResponse
from .models import User
 
import json
import bcrypt

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer

def add_cookies(response, user):
    refresh = RefreshToken.for_user(user)

    response.set_cookie(
        'access_token',
        str(refresh.access_token),
        max_age=3600,
        httponly=True
    )
    response.set_cookie(
        'refresh_token',
        str(refresh),
        max_age=86400,
        httponly=True
    )


@api_view(["GET"])
def get_all_users(request):
    print(request.headers)
    users = User.objects.all()
    return HttpResponse(users)

@api_view(["POST"])
def create_user(request):
    """
    POST /register

    Request Body:
    - firstName: str
    - lastName: str
    - password: str
    - email: str
    """
    body = request.body.decode("utf-8")
    body = json.loads(body)

    first_name = body["firstName"]
    last_name = body["lastName"]
    email = body["email"]
    password = body["password"]

    email_taken = User.objects.filter(email = email).exists()
    if email_taken:
        return HttpResponse("Emails already taken", status = 403)
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    new_user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password_hash = hashed_password, pfp_path = None)
    new_user.save()

    data = UserSerializer(new_user)

    response = Response(data.data, status=status.HTTP_201_CREATED)

    add_cookies(response, new_user)

    return response

@api_view(["POST"])
def login_user(request):
    body = request.body.decode("utf-8")
    body = json.loads(body)
    email = body["email"]
    password = body["password"]
    user = User.objects.filter(email = email).first()
    if not user: 
        return Response("Incorrect Email or Password", status=status.HTTP_401_UNAUTHORIZED) 

    isPasswordOk = bcrypt.checkpw(password.encode("utf-8"), user.password_hash.encode("utf-8"))
    if isPasswordOk:
        data = UserSerializer(user)

        response = Response(data.data, status=status.HTTP_201_CREATED)

        add_cookies(response, user)
        
        return response
    else: 
        return Response("Incorrect Email or Password", status=status.HTTP_401_UNAUTHORIZED) 


