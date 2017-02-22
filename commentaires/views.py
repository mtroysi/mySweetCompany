# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import redirect

from commentaires.forms import CommentForm
from commentaires.models import Commentaire
from produits.forms import ProductForm
from produits.models import Produit


# Create your views here.


def add_comment(request, id):
    if request.method == 'POST':
        new_comment = Commentaire()
        produit = Produit.objects.get(id=id)
        new_comment.text = request.POST.get('text')
        new_comment.auteur = request.user.client
        new_comment.produit = produit
        new_comment.save()
        messages.add_message(request, messages.INFO, 'Commentaire posté.')
    return redirect('/produit/'+str(id), {'form': ProductForm(), 'produit': produit, 'comment_form': CommentForm()})
