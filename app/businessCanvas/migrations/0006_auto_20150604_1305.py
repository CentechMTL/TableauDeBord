# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('businessCanvas', '0005_auto_20150604_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businesscanvaselement',
            old_name='newtype',
            new_name='type',
        ),
    ]
