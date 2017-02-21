# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from produits.models import Produit
from client.models import Client
from mySweetCompany.forms import ContactForm
from mySweetCompany.forms import InscriptionForm
from mySweetCompany.forms import LoginForm
from produits.forms import ProductForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout


def home(request):
    produits = Produit.objects.all().order_by('-date_publication')[:1]
    return render(request, 'home.html', {'produits': produits})


def login(request):
    form_class = LoginForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.add_message(request, messages.INFO, 'Bienvenue.')
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
            return redirect('/')
    return render(request, 'login.html', {'form': form_class})


def logout_view(request):
    logout(request)
    return redirect('/')


def inscription(request):
    form_class = InscriptionForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            client = Client()
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'],
                                            email=form.cleaned_data['mail'],
                                            first_name=form.cleaned_data['prenom'],
                                            last_name=form.cleaned_data['nom'])
            user.save()
            client.user = user
            client.age = request.POST.get('age', '')
            client.save()

            messages.add_message(request, messages.INFO, 'Inscription réussie.')
            return redirect('/')
    return render(request, 'inscription.html', {'form': form_class})


def produits(request):
    produits = Produit.objects.all()
    form_class = ProductForm
    return render(request, 'produits.html', {'produits': produits, 'form': form_class})


@login_required
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
