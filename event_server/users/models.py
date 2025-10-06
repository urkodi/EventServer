from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=254)
    password_hash = models.CharField()
    pfp_path = models.CharField()

    def __str__ (self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        app_label = 'users'
        db_table = 'users'