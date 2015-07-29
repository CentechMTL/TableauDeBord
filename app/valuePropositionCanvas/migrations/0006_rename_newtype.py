# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valuePropositionCanvas', '0005_delete_old_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='valuepropositioncanvaselement',
            old_name='newtype',
            new_name='type',
        ),
    ]
