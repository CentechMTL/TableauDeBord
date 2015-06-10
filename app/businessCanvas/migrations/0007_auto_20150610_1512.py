# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('businessCanvas', '0006_auto_20150604_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesscanvaselement',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 10, 15, 12, 29, 466000), verbose_name='Date of updated', auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='archive',
            name='company',
            field=models.ForeignKey(verbose_name='Company', to='company.Company'),
        ),
        migrations.AlterField(
            model_name='archive',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='archive',
            name='elements',
            field=models.ManyToManyField(to='businessCanvas.BusinessCanvasElement', verbose_name='Elements of the archive', blank=True),
        ),
        migrations.AlterField(
            model_name='businesscanvaselement',
            name='comment',
            field=models.TextField(max_length=2000, verbose_name='Comment', blank=True),
        ),
        migrations.AlterField(
            model_name='businesscanvaselement',
            name='company',
            field=models.ForeignKey(verbose_name='Company', to='company.Company'),
        ),
        migrations.AlterField(
            model_name='businesscanvaselement',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date of creation'),
        ),
        migrations.AlterField(
            model_name='businesscanvaselement',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='businesscanvaselement',
            name='type',
            field=models.CharField(max_length=20, null=True, verbose_name='Type', choices=[(b'KeyPartner', 1), (b'KeyActivitie', 2), (b'ValueProposition', 3), (b'CustomerRelationship', 4), (b'KeyResource', 5), (b'Channel', 6), (b'CustomerSegment', 7), (b'CostStructure', 8), (b'RevenueStream', 9), (b'BrainstormingSpace', 10)]),
        ),
    ]
