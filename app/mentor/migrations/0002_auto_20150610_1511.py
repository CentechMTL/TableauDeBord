# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='expertise',
            field=models.ManyToManyField(to='home.Expertise', verbose_name='Areas of expertise', blank=True),
        ),
    ]
