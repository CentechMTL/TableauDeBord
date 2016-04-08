# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floorMap', '0004_room_surface_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='pricing',
            field=models.DecimalField(default=b'0.00', help_text='Per sq. ft.', verbose_name='Pricing', max_digits=5, decimal_places=2),
        ),
    ]
