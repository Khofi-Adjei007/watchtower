from django.db import models

# Create your models here.
class portalUsers(models.Model):
    userName = models.CharField(max_length=100)
    details = models.CharField(max_length=250,default=0)


class practice_data(models.Model):
    username = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=14)
    report_details = models.CharField(max_length=20)
