# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floorMap', '0003_auto_20160322_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='surface_size',
            field=models.PositiveSmallIntegerField(help_text='Value in ft\xb2.', null=True, verbose_name='Surface size', blank=True),
        ),
    ]
