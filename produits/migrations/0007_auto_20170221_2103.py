# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0006_auto_20170221_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='vendeurs',
            new_name='vendeur',
        ),
    ]
