# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='produits',
            field=models.ManyToManyField(to='produits.Produit'),
        ),
        migrations.AlterField(
            model_name='client',
            name='date_inscription',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='client',
            name='mail',
            field=models.EmailField(max_length=254),
        ),
    ]
