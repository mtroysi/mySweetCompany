from django.shortcuts import render
from django.conf import settings
from produits.models import Produit

# def home(request):
#     name='Valou'
#     n=36
#     return render(request, 'base.html', {'name':name, 'n':n})


def home(request):
    produits = Produit.objects.all().order_by('-date_publication')[:10]
    return render(request, 'home.html', {'produits':produits})


def login(request):
    return render(request, 'connexion.html')


def inscription(request):
    return render(request, 'inscription.html')


def produits(request):
    produits = Produit.objects.all()
    return render(request, 'produits.html', {'produits':produits})


def panier(request):
    return render(request, 'panier.html')


def contact(request):
    return render(request, 'contact.html')


def credits(request):
    return render(request, 'credits.html')