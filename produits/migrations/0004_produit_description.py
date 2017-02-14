# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0003_auto_20170210_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='description',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
