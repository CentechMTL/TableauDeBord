# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0004_auto_20150727_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerexperiment',
            name='experiment_description',
            field=models.TextField(max_length=1024, verbose_name='Experiment description'),
        ),
        migrations.AlterField(
            model_name='customerexperiment',
            name='test_subject_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Number of test participants'),
        ),
        migrations.AlterField(
            model_name='customerexperiment',
            name='test_subject_description',
            field=models.TextField(max_length=512, verbose_name='Test description'),
        ),
    ]
