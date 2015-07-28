# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('businessCanvas', '0009_delete_businesscanvastype'),
        ('valuePropositionCanvas', '0007_delete_valuepropositioncanvastype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valuepropositioncanvaselement',
            name='company',
        ),
        migrations.AddField(
            model_name='valuepropositioncanvaselement',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 28, 11, 58, 14, 505000), verbose_name='Date of updated', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valuepropositioncanvaselement',
            name='valueProposition',
            field=models.ForeignKey(default=None, verbose_name='Value proposition', to='businessCanvas.BusinessCanvasElement'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='valuepropositioncanvaselement',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date of creation'),
        ),
    ]
