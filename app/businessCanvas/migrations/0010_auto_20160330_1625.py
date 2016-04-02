# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('businessCanvas', '0009_delete_businesscanvastype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='elements',
            field=models.ManyToManyField(to='businessCanvas.BusinessCanvasElement', verbose_name='Archive elements', blank=True),
        ),
        migrations.AlterField(
            model_name='businesscanvaselement',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='businesscanvaselement',
            name='disactivated',
            field=models.BooleanField(default=False, verbose_name='Deactivated'),
        ),
        migrations.AlterField(
            model_name='businesscanvaselement',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Update date'),
        ),
    ]
