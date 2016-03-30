# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20160225_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companystatus',
            options={'verbose_name': 'Company status', 'verbose_name_plural': 'Company status'},
        ),
    ]
