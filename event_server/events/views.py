from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Event
from .serializers import EventSerializer

# Create your views here.

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_event(request):
    print(request.headers)
    serializer = EventSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)