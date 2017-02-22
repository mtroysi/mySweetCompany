# -*- coding: utf-8 -*-
from carton.cart import Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from produits.forms import ProductForm
from commentaires.forms import CommentForm
from produits.models import Produit


# Create your views here.


def show(request, id):
    produit = Produit.objects.get(id=id)
    form_class = ProductForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            number = request.POST.get('product_number', '')
            cart = Cart(request.session)
            cart.add(produit, price=produit.prix, quantity=number)
            messages.add_message(request, messages.INFO, 'Produit ajouté au panier.')
    return render(request, 'show.html', {'produit': produit, 'form': form_class, 'comment_form': CommentForm()})


@login_required
def remove_from_cart(request, id):
    produit = Produit.objects.get(id=id)
    if produit is not None:
        cart = Cart(request.session)
        cart.remove(produit)
        messages.add_message(request, messages.INFO, 'Produit retiré du panier.')
    return render(request, 'panier.html')


@login_required
def add_to_cart(request, id):
    form_class = ProductForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            number = request.POST.get('product_number', '')
            produit = Produit.objects.get(id=id)
            if produit is not None:
                cart = Cart(request.session)
                cart.add(produit, price=produit.prix, quantity=number)
                messages.add_message(request, messages.INFO, 'Produit ajouté au panier.')
    return redirect("/produits")
