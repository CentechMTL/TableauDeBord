# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('businessCanvas', '0008_auto_20150610_1527'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BusinessCanvasType',
        ),
    ]
