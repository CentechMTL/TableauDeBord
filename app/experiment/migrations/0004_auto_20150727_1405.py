# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0003_auto_20150708_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerexperiment',
            name='dateFinish',
            field=models.DateTimeField(auto_now=True, verbose_name='End date'),
        ),
        migrations.AlterField(
            model_name='customerexperiment',
            name='dateStart',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Start date'),
        ),
    ]
