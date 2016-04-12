# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('floorMap', '0005_rent_pricing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('default_annual_rental_rate', models.DecimalField(default=b'0.00', help_text='Per sq. ft.', verbose_name='Default annual rental rate', max_digits=5, decimal_places=2)),
            ],
        ),
    ]
