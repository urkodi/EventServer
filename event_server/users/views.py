from django.http import HttpResponse
import json
import bcrypt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
from .models import User
from .serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


def add_cookies(response, user):
    refresh = RefreshToken.for_user(user)

    response.set_cookie(
        key="access_token",
        value=str(refresh.access_token),
        httponly=True,
        secure=True,         # REQUIRED for SameSite=None
        samesite="None",     # REQUIRED for cross-origin
        path="/",            # REQUIRED so everything gets the cookie
        domain="127.0.0.1",
        max_age=86400
    )

    response.set_cookie(
        key="refresh_token",
        value=str(refresh),
        httponly=True,
        secure=True,
        samesite="None",
        path="/",
        domain="127.0.0.1",
        max_age=86400
    )

    return response


def get_user_from_cookie(request):
    token = request.COOKIES.get("access_token")
    if not token:
        raise AuthenticationFailed("No access token found.")

    try:
        decoded = AccessToken(token)  # <--- FIXED
        user_id = decoded["user_id"]
        return user_id
    except Exception:
        raise AuthenticationFailed("Invalid or expired token.")
    

@api_view(["GET"])
def debug_cookies(request):
    print("COOKIES:", request.COOKIES)
    return Response(request.COOKIES)

from rest_framework.permissions import AllowAny
@api_view(["GET"])
@permission_classes([AllowAny])
def get_logged_in_user(request):
    user_id = get_user_from_cookie(request)
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(["GET"])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True, context={"request": request})
    return Response(serializer.data)

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

    email_taken = User.objects.filter(email=email).exists()
    if email_taken:
        return HttpResponse("Emails already taken", status=403)
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
        "utf-8"
    )

    new_user = User.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=hashed_password,
        pfp_path=None,
    )
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
    user = User.objects.filter(email=email).first()
    if not user:
        return Response(
            "Incorrect Email or Password", status=status.HTTP_401_UNAUTHORIZED
        )

    isPasswordOk = bcrypt.checkpw(
        password.encode("utf-8"), user.password.encode("utf-8")
    )
    if isPasswordOk:
        data = UserSerializer(user)

        response = Response(data.data, status=status.HTTP_201_CREATED)

        add_cookies(response, user)

        return response
    else:
        return Response(
            "Incorrect Email or Password", status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(["GET"])
def get_user_by_id(request):
    user_id = request.query_params.get("user")

    if not user_id:
        return Response({"error": "Missing 'user' query parameter"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, context={"request": request})
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def update_user(request):
    try:
        user_id = request.query_params.get("user")
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    serializer = UserSerializer(
        user,
        data=request.data,
        partial=True,
        context={"request": request}
    )

    if serializer.is_valid():
        serializer.save()

        # Handle file upload manually
        if "profilePicture" in request.FILES:
            user.pfp_path = request.FILES["profilePicture"]
            user.save()

        return Response(serializer.data, status=200)

    return Response(serializer.errors, status=400)