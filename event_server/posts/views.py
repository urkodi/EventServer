from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from users.models import User

# -------------------------------------
# Create a post
# -------------------------------------
@api_view(["POST"])
def create_post(request):
    user_id = request.data.get("user")
    description = request.data.get("description")

    if not user_id or not description:
        return Response({"error": "Missing user or description"}, status=400)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    serializer = PostSerializer(data={"description": description})
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


# -------------------------------------
# Get ALL posts
# -------------------------------------
@api_view(["GET"])
def all_posts(request):
    posts = Post.objects.all().order_by("-created_at")
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


# -------------------------------------
# Get posts by USER
# -------------------------------------
@api_view(["GET"])
def posts_by_user(request):
    user_id = request.query_params.get("user")

    if not user_id:
        return Response({"error": "Missing user id"}, status=400)

    posts = Post.objects.filter(user_id=user_id).order_by("-created_at")
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
