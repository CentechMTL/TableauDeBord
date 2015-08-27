# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_company_endofincubation'),
    ]

    operations = [
        migrations.AddField(
            model_name='companystatus',
            name='comment',
            field=models.TextField(verbose_name='Comment', blank=True),
        ),
    ]
