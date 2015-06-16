# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='updated',
            field=models.DateTimeField(blank=True),
        ),
    ]
