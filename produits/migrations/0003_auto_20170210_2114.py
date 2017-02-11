# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0002_auto_20170209_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auteur', models.CharField(max_length=1024)),
                ('date_publication', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='date_publication',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='produit',
            name='note',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commentaire',
            name='produit',
            field=models.ForeignKey(to='produits.Produit'),
        ),
    ]
