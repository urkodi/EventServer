from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=254)
    password_hash = models.CharField()
    pfp_path = models.CharField(default= None, blank= True, null= True)

    def __str__ (self):
        return f"{self.first_name} {self.last_name}"
    
class UserInteractions(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default= None, blank= True, null= True)

class UserBookmarks(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default= None, blank= True, null= True)

class UserTickets(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default= None, blank= True, null= True)

    
