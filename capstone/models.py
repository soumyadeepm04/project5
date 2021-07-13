from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model

# Create your models here.

class User(AbstractUser):
    pass

class Events(models.Model):
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.CharField(max_length=500, null=True)
    venue = models.CharField(max_length=250, null=True)
    registered = models.IntegerField(null = True)

class Register(models.Model):
    registered_event_id = models.IntegerField(null=True)
    registered_user = models.ForeignKey("User", on_delete=models.CASCADE)

class Authorize(models.Model):
    comment = models.CharField(max_length=500)
    event_id = models.IntegerField()
    event_owner = models.ForeignKey("User", on_delete=models.CASCADE, null = True)

class Authorized(models.Model):
    comment = models.CharField(max_length=500)
    event_id = models.IntegerField()