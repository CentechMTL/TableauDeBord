# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floorMap', '0002_auto_20160321_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(max_length=10, verbose_name='Room code'),
        ),
        migrations.AlterField(
            model_name='room',
            name='coords',
            field=models.CommaSeparatedIntegerField(help_text='<b>Rectangle:</b> Please use the following format: <em>x1,y1,x2,y2</em><br /><b>Polygon:</b> Please use the following format: <em>x1,y1,...,xn,yn</em>', max_length=2000, verbose_name='Coordinates'),
        ),
        migrations.AlterField(
            model_name='room',
            name='static_label',
            field=models.CharField(help_text='<b>Warning:</b> Will be overwritten by rental owner name.', max_length=100, verbose_name='Label', blank=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='text_coords',
            field=models.CommaSeparatedIntegerField(help_text='Area where the label will be displayed (defaults to room coordinates)<br /><em>x1,y1,x2,y2</em>. <b>Rectangle only!</b>', max_length=50, null=True, verbose_name='Text area coordinates', blank=True),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='alt_bg_color',
            field=models.CharField(help_text='Used for type state change (e.g. occupied rental)<br>Please use the following format: #FFFFFF', max_length=7, verbose_name='Alternative background color', blank=True),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Description', blank=True),
        ),
    ]
