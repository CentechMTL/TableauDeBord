# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0011_auto_20150708_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='company',
            field=models.ForeignKey(related_name='KPIs', verbose_name='Companies', to='company.Company'),
        ),
    ]
