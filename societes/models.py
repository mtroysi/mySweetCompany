from django.db import models

# Create your models here.

class Societe(models.Model):
    nom = models.CharField(max_length=1024)
    mail = models.EmailField()