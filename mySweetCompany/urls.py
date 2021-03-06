"""mySweetCompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from mySweetCompany.feeds import LatestProductsFeed

urlpatterns = [
    url(r'^comment/new/(?P<id>[0-9]+)', 'commentaires.views.add_comment', name='add_comment'),
    url(r'^produits', 'mySweetCompany.views.produits', name='produits'),
    url(r'^produit/(?P<id>[0-9]+)/remove', 'produits.views.remove_from_cart', name='remove_from_cart'),
    url(r'^produit/(?P<id>[0-9]+)/add', 'produits.views.add_to_cart', name='add_to_cart'),
    url(r'^produit/(?P<id>[0-9]+)/$', 'produits.views.show', name='show'),
    url(r'^panier', 'mySweetCompany.views.panier', name='panier'),
    url(r'^inscription', 'mySweetCompany.views.inscription', name='inscription'),
    url(r'^logout', 'mySweetCompany.views.logout_view', name='logout'),
    url(r'^accounts/login/$', 'mySweetCompany.views.login', name='login'),
    url(r'^contact', 'mySweetCompany.views.contact', name='contact'),
    url(r'^credits', 'mySweetCompany.views.credits', name='credits'),
    url(r'^latest', LatestProductsFeed(), name="latest"),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mySweetCompany.views.home', name='home'),
]
