# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerExperiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateStart', models.DateField(auto_now_add=True, verbose_name='Start date')),
                ('dateFinish', models.DateField(auto_now=True, verbose_name='End date')),
                ('hypothesis', models.TextField(max_length=512, verbose_name='Hypothesis')),
                ('validated', models.NullBooleanField(verbose_name='Validation')),
                ('experiment_description', models.TextField(max_length=1024, verbose_name='Description of the experiment')),
                ('test_subject_count', models.PositiveIntegerField(default=0, verbose_name='Number of subject for the test')),
                ('test_subject_description', models.TextField(max_length=512, verbose_name='Description of the subject test')),
                ('conclusions', models.TextField(max_length=512, verbose_name='Conclusion', blank=True)),
                ('company', models.ForeignKey(to='company.Company')),
            ],
        ),
    ]
