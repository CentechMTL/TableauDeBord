# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20150623_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(null=True, verbose_name='Facebook', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='googlePlus',
            field=models.URLField(null=True, verbose_name='Google+', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linkedIn',
            field=models.URLField(null=True, verbose_name='linkedIn', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter',
            field=models.URLField(null=True, verbose_name='Twitter', blank=True),
        ),
    ]
