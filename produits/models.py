from django.db import models
from societes.models import Societe
from django.utils import timezone

# Create your models here.

class Produit(models.Model):
    nom = models.CharField(max_length=1024)
    prix = models.FloatField()
    note = models.FloatField()
    description = models.CharField(max_length=1024, null=True)
    date_publication = models.DateTimeField(default=timezone.now)
    vendeurs = models.ManyToManyField(Societe)

class Commentaire(models.Model):
    auteur = models.CharField(max_length=1024)
    produit = models.ForeignKey("Produit")
    date_publication = models.DateTimeField(default=timezone.now)
    text = models.TextField()