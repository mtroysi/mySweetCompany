# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=1024)),
                ('prenom', models.CharField(max_length=1024)),
                ('age', models.IntegerField()),
                ('mail', models.EmailField(max_length=1024)),
                ('date_inscription', models.DateTimeField(verbose_name=b'date inscription')),
            ],
        ),
    ]
