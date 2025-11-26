from enum import unique
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    password = models.CharField()
    pfp_path = models.CharField(default=None, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "password"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class UserInteractions(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey("events.Event", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=None, blank=True, null=True)


class UserBookmarks(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey("events.Event", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=None, blank=True, null=True)


class UserTickets(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey("events.Event", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=None, blank=True, null=True)
