# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0002_auto_20150708_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerexperiment',
            name='company',
            field=models.ForeignKey(related_name='experiments', verbose_name='Company', to='company.Company'),
        ),
    ]
