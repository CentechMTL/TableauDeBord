# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_company_incubated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='facebook',
            field=models.URLField(null=True, verbose_name='Facebook', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='googlePlus',
            field=models.URLField(null=True, verbose_name='Google+', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='linkedIn',
            field=models.URLField(null=True, verbose_name='linkedIn', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='twitter',
            field=models.URLField(null=True, verbose_name='Twitter', blank=True),
        ),
    ]
