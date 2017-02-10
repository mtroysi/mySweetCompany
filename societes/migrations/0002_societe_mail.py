# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='societe',
            name='mail',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
