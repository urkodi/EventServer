from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Review
from .serializers import ReviewSerializer
from events.models import Event
from users.models import User


# ---------------------------------------------
# 1. Save Review (POST)
# ---------------------------------------------
@api_view(["POST"])
def create_review(request):
    try:
        user_id = request.data.get("user")
        event_id = request.data.get("event")

        if not user_id or not event_id:
            return Response({"error": "Missing user or event id"}, status=400)

        user = User.objects.get(id=user_id)
        event = Event.objects.get(id=event_id)

        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user, event=event)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=400)

    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=404)


# ---------------------------------------------
# 2. Get ALL reviews (GET)
# ---------------------------------------------
@api_view(["GET"])
def get_all_reviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


# ---------------------------------------------
# 3. Get all reviews for a specific USER (GET)
# ---------------------------------------------
@api_view(["GET"])
def get_reviews_by_user(request):
    user_id = request.query_params.get("user")

    if not user_id:
        return Response({"error": "Missing 'user' query parameter"}, status=400)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    reviews = Review.objects.filter(user=user)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)