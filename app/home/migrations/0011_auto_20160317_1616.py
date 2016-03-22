# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_delete_floorplan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='company',
        ),
        migrations.RemoveField(
            model_name='rent',
            name='room',
        ),
        migrations.RemoveField(
            model_name='room',
            name='type',
        ),
        migrations.DeleteModel(
            name='Rent',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='RoomType',
        ),
    ]
