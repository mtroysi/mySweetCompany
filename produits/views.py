from django.shortcuts import render
from produits.models import Produit

# Create your views here.


def show(request, id):
    produit = Produit.objects.get(id=id)
    return render(request, 'show.html', {'produit':produit})