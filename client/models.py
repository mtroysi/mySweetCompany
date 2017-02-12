from django.db import models

from produits.models import Produit
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Client(models.Model):
	user = models.OneToOneField(User, null=True)
	nom = models.CharField(max_length=1024)
	prenom = models.CharField(max_length=1024)
	age = models.IntegerField()
	mail = models.EmailField(unique=True)
	date_inscription = models.DateTimeField(default=timezone.now)
	produits = models.ManyToManyField(Produit, blank=True)