# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0009_delete_kpitype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kpi',
            name='phase',
        ),
    ]
