# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valuePropositionCanvas', '0004_suppression_null_true'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ValuePropositionCanvasElement',
            name='type',
        ),
    ]
