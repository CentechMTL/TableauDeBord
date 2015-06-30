# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0007_auto_20150630_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kpi',
            old_name='newtype',
            new_name='type',
        ),
    ]
