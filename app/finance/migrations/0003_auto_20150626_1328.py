# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20150610_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bourse',
            name='company',
            field=models.ForeignKey(related_name='grants', verbose_name='Company', to='company.Company'),
        ),
        migrations.AlterField(
            model_name='investissement',
            name='company',
            field=models.ForeignKey(related_name='investments', verbose_name='Company', to='company.Company'),
        ),
        migrations.AlterField(
            model_name='pret',
            name='company',
            field=models.ForeignKey(related_name='loans', verbose_name='Company', to='company.Company'),
        ),
        migrations.AlterField(
            model_name='subvention',
            name='company',
            field=models.ForeignKey(related_name='subsidies', verbose_name='Company', to='company.Company'),
        ),
        migrations.AlterField(
            model_name='vente',
            name='company',
            field=models.ForeignKey(related_name='sales', verbose_name='Company', to='company.Company'),
        ),
    ]
