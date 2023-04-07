from django.db import models
from datetime import datetime

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=30)
    grade = models.CharField(max_length=100)


class Person(models.Model):
    username = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    mobile = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=15, blank=True)
    organ_pledged = models.CharField(max_length=100, blank=True)
    blood_group = models.CharField(max_length=25, blank=True)
    date= models.DateTimeField(default=datetime.now)
