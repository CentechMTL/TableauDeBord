# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0012_auto_20150708_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='period_start',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date'),
        ),
    ]
