from django.db import models
from societes.models import Societe

# Create your models here.

class Produit(models.Model):
    nom = models.CharField(max_length=1024)
    prix = models.FloatField()
    vendeurs = models.ManyToManyField(Societe)