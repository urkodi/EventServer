from django.db import models

class Review(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)

    # Snapshot fields — store event data at time of review
    event_title = models.CharField(max_length=255, null=True, blank=True)
    event_image = models.CharField(max_length=500, null=True, blank=True)

    stars = models.IntegerField(default=None, blank=True, null=True)
    description = models.TextField(max_length=2048, default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Automatically fill in event_title and event_image if missing.
        Ensures old reviews still show correct info even if event updates.
        """
        if self.event:
            if not self.event_title:
                self.event_title = self.event.title

            # Event model likely has `imageUrl` or `imagePath`
            event_img = None
            if hasattr(self.event, "imageUrl") and self.event.imageUrl:
                event_img = self.event.imageUrl
            elif hasattr(self.event, "imagePath") and self.event.imagePath:
                event_img = self.event.imagePath

            if event_img and not self.event_image:
                self.event_image = event_img

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Review by User {self.user_id} for Event {self.event_id}"
