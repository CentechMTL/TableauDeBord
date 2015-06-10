# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('founder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founder',
            name='about',
            field=models.CharField(max_length=2000, verbose_name='About', blank=True),
        ),
        migrations.AlterField(
            model_name='founder',
            name='equity',
            field=models.FloatField(default=0, verbose_name='Equity', blank=True),
        ),
    ]
