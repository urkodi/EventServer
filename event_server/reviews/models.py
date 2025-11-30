from django.db import models

class Review(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    stars = models.IntegerField(default=None, blank=True, null=True)
    description = models.TextField(max_length= 2048, default= None, blank= True, null= True)