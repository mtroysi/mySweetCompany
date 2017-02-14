# -*- coding: utf-8 -*-
from django import forms


class ProductForm(forms.Form):
    product_number = forms.IntegerField(min_value=1, initial=1, label='Nombre ')