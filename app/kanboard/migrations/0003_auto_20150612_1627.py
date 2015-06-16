# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanboard', '0002_auto_20150612_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='created',
            field=models.DateTimeField(blank=True),
        ),
    ]
