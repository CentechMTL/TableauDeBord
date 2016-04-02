# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floorMap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomtype',
            name='alt_bg_color',
            field=models.CharField(help_text='Used for type state change (e.g. occupied rental)<br />Please use the following format: #FFFFFF', max_length=7, verbose_name='Alternative background color', blank=True),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='bg_color',
            field=models.CharField(default=b'#FFFFFF', help_text='Please use the following format: #FFFFFF', max_length=7, verbose_name='Background color'),
        ),
    ]
