from django.contrib import admin
from produits.models import Produit
from produits.models import Commentaire

# Register your models here.
admin.site.register(Produit)
admin.site.register(Commentaire)