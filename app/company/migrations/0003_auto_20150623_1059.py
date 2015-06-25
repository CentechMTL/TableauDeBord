# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20150610_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='founders',
            field=models.ManyToManyField(related_name='company', verbose_name='Founders', to='founder.Founder', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='mentors',
            field=models.ManyToManyField(related_name='company', verbose_name='Mentors', to='mentor.Mentor', blank=True),
        ),
    ]
