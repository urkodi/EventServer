from django.urls import path
from . import views

urlpatterns = [
    path("create", views.create_review, name="create_review"),
    path("all", views.get_all_reviews, name="all_reviews"),
    path("by_user", views.get_reviews_by_user, name="reviews_by_user"),
]
