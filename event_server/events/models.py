from django.db import models

class Event(models.Model):
    owner_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField(max_length= 2048, default= None, blank= True, null= True)
    image_path = models.CharField(default= None, blank= True, null= True)
    timestamp = models.DateTimeField(default= None, blank= True, null= True)
    address = models.CharField(max_length=256, default= None, blank= True, null= True)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class EventUsers(models.Model):
    owner_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    rank = models.PositiveSmallIntegerField(default= 0)


