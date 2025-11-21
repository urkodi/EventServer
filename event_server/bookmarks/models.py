from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.IntegerField()  
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    image = models.URLField()
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} bookmarked by {self.user.username}"
