# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanboard', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='phase',
            field=models.CharField(max_length=50, verbose_name='Phase', choices=[(1, 'Commercialisation'), (2, 'D\xe9veloppement de produit'), (3, 'Financement'), (4, 'Gouvernance')]),
        ),
    ]
