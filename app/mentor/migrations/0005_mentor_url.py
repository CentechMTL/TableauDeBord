# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0004_auto_20150706_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='url',
            field=models.URLField(null=True, verbose_name='URL', blank=True),
        ),
    ]
