from django.shortcuts import render
from django.conf import settings
from client.models import Client

def home(request):
    name='Valou'
    n=36
    return render(request, 'base.html', {'name':name, 'n':n})

def clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients':clients})