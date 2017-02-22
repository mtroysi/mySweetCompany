# -*- coding: utf-8 -*-
from django import forms
from .models import Commentaire


class CommentForm(forms.Form):
    text = forms.CharField(max_length=1024, label='Votre commentaire ', required=True, widget=forms.Textarea)
