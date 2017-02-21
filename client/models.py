from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

class Client(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	age = models.IntegerField()
	date_inscription = models.DateTimeField(default=timezone.now)
