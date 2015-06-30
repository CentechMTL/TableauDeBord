# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0008_auto_20150630_1114'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KpiType',
        ),
    ]
