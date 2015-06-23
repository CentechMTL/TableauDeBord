# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('founder', '0002_auto_20150610_1511'),
        ('kanboard', '0005_auto_20150616_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='assigned',
            field=models.ForeignKey(related_name='cards', blank=True, to='founder.Founder', null=True),
        ),
    ]
