# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KPI',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('period_start', models.DateField(auto_now_add=True)),
                ('comment', models.TextField(default=b'', blank=True)),
                ('company', models.ForeignKey(to='company.Company')),
                ('phase', models.ForeignKey(to='company.CompanyStatus')),
            ],
        ),
        migrations.CreateModel(
            name='KpiType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='kpi',
            name='type',
            field=models.ForeignKey(to='kpi.KpiType'),
        ),
    ]
