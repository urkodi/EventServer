from django.db import models

class Event(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField(max_length= 2048, default= None, blank= True, null= True)
    category = models.TextField(max_length=80, default=None, blank=True, null=True)
    image_path = models.ImageField(upload_to="event_images/", blank=True, null=True)
    date = models.CharField(max_length=100, blank= True, null= True)
    time = models.CharField(max_length=100, blank= True, null= True)
    address = models.CharField(max_length=100,blank= True, null= True)
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    max_attendees = models.IntegerField(default=100)

class EventUsers(models.Model):
    owner_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    rank = models.PositiveSmallIntegerField(default= 0)

class Links(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    link = models.URLField(max_length=500)

class Categories(models.Model):
    name = models.CharField(max_length=64)

class EventCategories(models.Model):
     event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
     categories_id = models.ForeignKey(Categories, on_delete=models.CASCADE)

class Tags(models.Model):
    name = models.CharField(max_length=128)

class Forum(models.Model):
    owner_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    body = models.TextField(max_length= 2048, default= None, blank= True, null= True)
    timestamp = models.DateTimeField(default= None, blank= True, null= True)

class ForumComments(models.Model):
    forum_id = models.ForeignKey('events.Forum', on_delete=models.CASCADE)
    owner_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    body = models.TextField(max_length= 2048, default= None, blank= True, null= True)
    timestamp = models.DateTimeField(default= None, blank= True, null= True)


