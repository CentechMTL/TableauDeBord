# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valuePropositionCanvas', '0006_rename_newtype'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ValuePropositionCanvasType',
        ),
    ]
