from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class portalUsers(models.Model):
    userName = models.CharField(max_length=100)
    details = models.CharField(max_length=250,default=0)


class practice_data(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=14)
    password = models.CharField(max_length=10, default='')
    password_two = models.CharField(max_length=10, default='')

    def clean_data(self):
        if not self.username:
            raise ValidationError({'Username': 'Username cannot be empty'})
