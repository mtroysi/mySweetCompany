# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from produits.models import Produit
from mySweetCompany.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages


# def home(request):
#     name='Valou'
#     n=36
#     return render(request, 'base.html', {'name':name, 'n':n})


def home(request):
    produits = Produit.objects.all().order_by('-date_publication')[:10]
    return render(request, 'home.html', {'produits': produits})


def login(request):
    return render(request, 'connexion.html')


def inscription(request):
    return render(request, 'inscription.html')


def produits(request):
    produits = Produit.objects.all()
    return render(request, 'produits.html', {'produits': produits})


def panier(request):
    return render(request, 'panier.html')


def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['youremail@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            messages.add_message(request, messages.INFO, 'Message envoyé.')
            return redirect('contact')
    return render(request, 'contact.html', {'form': form_class})


def credits(request):
    return render(request, 'credits.html')
