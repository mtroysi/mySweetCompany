# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib import messages
from produits.models import Produit
from produits.forms import ProductForm


# Create your views here.


def show(request, id):
    produit = Produit.objects.get(id=id)
    form_class = ProductForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            number = request.POST.get('product_number', '')
            print 'Produit ' + str(produit.id) + ' ajouté ' + str(number) + ' fois'
            messages.add_message(request, messages.INFO, 'Produit ajouté au panier.')

    return render(request, 'show.html', {'produit': produit, 'form':form_class})
