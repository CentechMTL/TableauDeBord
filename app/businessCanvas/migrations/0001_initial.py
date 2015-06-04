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
            model_name='businesscanvaselement',
            name='type',
            field=models.ForeignKey(verbose_name='Type', to='businessCanvas.BusinessCanvasType'),
        ),
        migrations.AddField(
            model_name='archive',
            name='elements',
            field=models.ManyToManyField(to='businessCanvas.BusinessCanvasElement', blank=True),
        ),
    ]
