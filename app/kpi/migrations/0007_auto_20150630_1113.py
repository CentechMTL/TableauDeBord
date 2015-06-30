# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0006_auto_20150630_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kpi',
            name='type',
        ),
        migrations.AlterField(
            model_name='kpi',
            name='newtype',
            field=models.CharField(max_length=50, verbose_name='Type', choices=[(b'IRL', 1), (b'TRL', 2)]),
        ),
    ]
