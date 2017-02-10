# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20170209_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='produits',
            field=models.ManyToManyField(to='produits.Produit', blank=True),
        ),
    ]
