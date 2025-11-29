from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer, EventUsersSerializer
from .models import Event, EventUsers

@api_view(['POST'])
def create_event(request):
    serializer = EventSerializer(data=request.data, context={"request": request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    print("❌ Serializer errors:", serializer.errors) 
    return Response(serializer.errors, status=400)


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

