# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanboard', '0004_card_datelimit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='dateLimit',
            new_name='deadline',
        ),
    ]
