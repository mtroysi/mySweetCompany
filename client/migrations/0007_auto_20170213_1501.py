# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_client_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='client',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='client',
            name='prenom',
        ),
    ]
