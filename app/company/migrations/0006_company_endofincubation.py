# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20150706_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='endOfIncubation',
            field=models.DateField(null=True, blank=True),
        ),
    ]
