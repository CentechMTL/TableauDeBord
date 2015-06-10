# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('businessCanvas', '0007_auto_20150610_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date'),
        ),
    ]
