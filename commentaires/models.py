from django.db import models
from django.utils import timezone

from client.models import Client
from produits.models import Produit


# Create your models here.


class Commentaire(models.Model):
    auteur = models.ForeignKey(Client)
    produit = models.ForeignKey(Produit, related_name='comments')
    date_publication = models.DateTimeField(default=timezone.now)
    text = models.TextField()