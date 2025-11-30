from enum import unique
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    pfp_path = models.ImageField(upload_to="pfp_images/", blank=True, null=True)
    phone_number = models.TextField(max_length=100, blank=True, null=True)
    timezone = models.TextField(max_length=100, blank=True, null=True)
    location = models.TextField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=2048, blank=True, null=True)
    username = models.TextField(max_length=100, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

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
