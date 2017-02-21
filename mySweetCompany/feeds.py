# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from produits.models import Produit
from django.core.urlresolvers import reverse

class LatestProductsFeed(Feed):
    title = "Dernier produit ajouté"
    link = "/latest/"
    description = "Dernier produit ajouté sur My Sweet Company"

    def items(self):
        return Produit.objects.all().order_by('-date_publication')[:1]

    def item_title(self, item):
        return item.nom

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('show', kwargs = {'id':item.id})