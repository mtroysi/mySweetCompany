# -*- coding: utf-8 -*-
from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Votre nom :"
        self.fields['contact_email'].label = "Votre adresse mail :"
        self.fields['content'].label = "Votre message :"


class InscriptionForm(forms.Form):
    username = forms.CharField(max_length=1024, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    nom = forms.CharField(max_length=1024, required=True)
    prenom = forms.CharField(max_length=1024, required=True)
    age = forms.IntegerField(required=True)
    mail = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(InscriptionForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Pseudo :"
        self.fields['password'].label = "Mot de passe :"
        self.fields['nom'].label = "Nom :"
        self.fields['prenom'].label = "Prénom :"
        self.fields['age'].label = "Âge :"
        self.fields['mail'].label = "Adresse e-mail :"


class LoginForm(forms.Form):
    username = forms.CharField(max_length=1024, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Pseudo :"
        self.fields['password'].label = "Mot de passe :"


class SearchForm(forms.Form):
    search_text = forms.CharField(max_length=1024, label='Rechercher parmi les produits disponibles ')
