# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_remove_client_produits'),
        ('produits', '0007_auto_20170221_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_publication', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField()),
                ('auteur', models.ForeignKey(to='client.Client')),
                ('produit', models.ForeignKey(to='produits.Produit')),
            ],
        ),
    ]
