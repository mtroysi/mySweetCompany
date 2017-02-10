# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societes', '0002_societe_mail'),
        ('produits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='prix',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produit',
            name='vendeurs',
            field=models.ManyToManyField(to='societes.Societe'),
        ),
    ]
