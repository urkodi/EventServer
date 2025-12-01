from django.db import models
from django.conf import settings
from events.models import Event

class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookmarks")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="bookmarked_by", null=True, blank=True)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "event")

    def __str__(self):
        return f"{self.user} bookmarked {self.event}"
