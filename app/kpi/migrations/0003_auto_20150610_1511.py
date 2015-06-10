# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0002_auto_20150604_1022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kpi',
            options={'verbose_name_plural': 'KPIs'},
        ),
        migrations.AlterModelOptions(
            name='kpitype',
            options={'verbose_name_plural': 'Types of KPI'},
        ),
        migrations.AlterField(
            model_name='kpi',
            name='comment',
            field=models.TextField(default=b'', verbose_name='Comment', blank=True),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='company',
            field=models.ForeignKey(verbose_name='Companies', to='company.Company'),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='level',
            field=models.IntegerField(verbose_name='Level', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='period_start',
            field=models.DateField(auto_now_add=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='phase',
            field=models.ForeignKey(verbose_name='Status', to='company.CompanyStatus'),
        ),
        migrations.AlterField(
            model_name='kpi',
            name='type',
            field=models.ForeignKey(verbose_name='Type of KPI', to='kpi.KpiType'),
        ),
        migrations.AlterField(
            model_name='kpitype',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]
