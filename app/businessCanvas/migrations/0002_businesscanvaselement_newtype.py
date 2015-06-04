# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('businessCanvas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesscanvaselement',
            name='newtype',
            field=models.CharField(max_length=20, null=True, choices=[(1, b'KeyPartner'), (2, b'KeyActivitie'), (3, b'ValueProposition'), (4, b'CustomerRelationship'), (5, b'KeyResource'), (6, b'Channel'), (7, b'CustomerSegment'), (8, b'CostStructure'), (9, b'RevenueStream'), (10, b'BrainstormingSpace')]),
        ),
    ]
