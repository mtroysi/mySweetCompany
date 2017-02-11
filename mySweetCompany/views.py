from django.shortcuts import render
from django.conf import settings
from client.models import Client

# def home(request):
#     name='Valou'
#     n=36
#     return render(request, 'base.html', {'name':name, 'n':n})

def home(request):
    return render(request, 'home.html')

# def clients(request):
#     clients = Client.objects.all()
#     return render(request, 'clients.html', {'clients':clients})

def login(request):
    return render(request, 'connexion.html')

def inscription(request):
    return render(request, 'inscription.html')

def produits(request):
    return render(request, 'produits.html')

def panier(request):
    return render(request, 'panier.html')

def contact(request):
    return render(request, 'contact.html')

def credits(request):
    return render(request, 'credits.html')