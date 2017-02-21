from django.db import models
from django.utils import timezone
from societes.models import Societe

# Create your models here.

class Produit(models.Model):
    nom = models.CharField(max_length=1024)
    prix = models.FloatField()
    description = models.CharField(max_length=1024, null=True)
    date_publication = models.DateTimeField(default=timezone.now)
    vendeur = models.ForeignKey(Societe)

