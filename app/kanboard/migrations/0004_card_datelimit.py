# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanboard', '0003_auto_20150612_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='dateLimit',
            field=models.DateField(null=True, blank=True),
        ),
    ]
