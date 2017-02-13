from django.db import models

from produits.models import Produit
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Client(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	age = models.IntegerField()
	date_inscription = models.DateTimeField(default=timezone.now)
	produits = models.ManyToManyField(Produit, blank=True)