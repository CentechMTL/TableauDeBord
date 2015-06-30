# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0005_auto_20150630_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='newtype',
            field=models.CharField(max_length=20, verbose_name='Type', choices=[(b'IRL', 1), (b'TRL', 2)]),
        ),
    ]
