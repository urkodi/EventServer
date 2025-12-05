from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import status

from django.db.models import Q 

from users.authentication import JWTCookieAuthentication
from .serializers import EventSerializer, EventUsersSerializer
from .models import Event, EventUsers

@api_view(['POST'])
@authentication_classes([JWTCookieAuthentication])
@permission_classes([IsAuthenticated])
def create_event(request):
    owner_id = request.user.id

    if owner_id is None:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    data = request.data
    data["owner"] = owner_id

    serializer = EventSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    print("Serializer errors:", serializer.errors) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_events(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True, context={"request": request})
    return Response(serializer.data)

@api_view(['GET'])
def list_events_by_owner(request):
    owner_id = request.query_params.get("owner")
    events = Event.objects.filter(owner_id=owner_id)
    serializer = EventSerializer(events, many=True, context={"request": request})
    return Response(serializer.data)

@api_view(['GET'])
def search_events(request):
    events = Event.objects.all()
    search_query = request.query_params.get('q', None)
    category = request.query_params.get('category', None)
    date = request.query_params.get('date', None)

    if search_query:
        events = events.filter(
            Q(name__icontains=search_query) |        
            Q(address__icontains=search_query)       
        )
    
    if category:
        events = events.filter(category=category)
    
    if date:
        events = events.filter(date=date)
    
    serializer = EventSerializer(events, many=True, context={"request": request})
    return Response(serializer.data)