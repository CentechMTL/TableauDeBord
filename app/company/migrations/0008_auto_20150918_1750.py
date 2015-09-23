# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_companystatus_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presence',
            name='company',
            field=models.ManyToManyField(to='company.Company', verbose_name='Companies'),
        ),
        migrations.AlterField(
            model_name='presence',
            name='date',
            field=models.DateTimeField(verbose_name='Date'),
        ),
    ]
