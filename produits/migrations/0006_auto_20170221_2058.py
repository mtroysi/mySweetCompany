# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societes', '0002_societe_mail'),
        ('produits', '0005_remove_produit_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='produit',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='vendeurs',
        ),
        migrations.AddField(
            model_name='produit',
            name='vendeurs',
            field=models.ForeignKey(default=1, to='societes.Societe'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Commentaire',
        ),
    ]
