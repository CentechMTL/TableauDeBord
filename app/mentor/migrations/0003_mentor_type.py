# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0002_auto_20150610_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='type',
            field=models.CharField(max_length=20, null=True, verbose_name='Type', choices=[(b'Finance', 1), (b'Technologie', 2)]),
        ),
    ]
