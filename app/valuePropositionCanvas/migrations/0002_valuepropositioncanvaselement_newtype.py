# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valuePropositionCanvas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='valuepropositioncanvaselement',
            name='newtype',
            field=models.CharField(max_length=20, null=True, verbose_name='Type', choices=[(b'Gain', b'Gain'), (b'Pain', b'Pain'), (b'customerJob', b'customerJob'), (b'GainCreator', b'GainCreator'), (b'PainReliever', b'PainReliever'), (b'ProductAndService', b'ProductAndService')]),
        ),
    ]
