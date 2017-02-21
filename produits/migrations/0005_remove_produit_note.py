# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0004_produit_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='note',
        ),
    ]
