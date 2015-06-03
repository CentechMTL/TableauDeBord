# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('company', models.ForeignKey(to='company.Company')),
            ],
            options={
                'verbose_name': 'Archive',
            },
        ),
        migrations.CreateModel(
            name='BusinessCanvasElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('comment', models.TextField(max_length=2000, blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(db_index=True, max_length=20, verbose_name='Type', choices=[(b'KeyPartner', b'KeyPartner'), (b'KeyActivitie', b'KeyActivitie'), (b'ValueProposition', b'ValueProposition'), (b'CustomerRelationship', b'CustomerRelationship'), (b'KeyResource', b'KeyResource'), (b'Channel', b'Channel'), (b'CustomerSegment', b'CustomerSegment'), (b'CostStructure', b'CostStructure'), (b'RevenueStream', b'RevenueStream'), (b'BrainstormingSpace', b'BrainstormingSpace')])),
                ('disactivated', models.BooleanField(default=False, verbose_name='Disactivated')),
                ('company', models.ForeignKey(to='company.Company')),
            ],
            options={
                'verbose_name': 'Business canvas element',
            },
        ),
        migrations.CreateModel(
            name='BusinessCanvasType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Business canvas type',
            },
        ),
        migrations.AddField(
            model_name='archive',
            name='elements',
            field=models.ManyToManyField(to='businessCanvas.BusinessCanvasElement', blank=True),
        ),
    ]
