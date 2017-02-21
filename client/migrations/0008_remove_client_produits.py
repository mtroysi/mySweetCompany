# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_auto_20170213_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='produits',
        ),
    ]
