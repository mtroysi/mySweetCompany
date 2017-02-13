# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20170209_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='date_inscription',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='client',
            name='mail',
            field=models.EmailField(unique=True, max_length=254),
        ),
    ]
