from django.db import models

class Post(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="posts")
    description = models.TextField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.user.username}"