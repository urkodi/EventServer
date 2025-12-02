from django.urls import path
from . import views

urlpatterns = [
    path("create", views.create_post),
    path("all", views.all_posts),
    path("user", views.posts_by_user),
]
