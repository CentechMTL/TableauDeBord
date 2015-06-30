# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0003_auto_20150610_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='kpi',
            name='newtype',
            field=models.CharField(max_length=20, null=True, verbose_name='Type', choices=[(b'IRL', 1), (b'TRL', 2)]),
        ),
    ]
