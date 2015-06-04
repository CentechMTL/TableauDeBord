# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('businessCanvas', '0004_auto_20150604_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businesscanvaselement',
            name='type',
        ),
    ]
