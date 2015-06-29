# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20150623_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='incubated_on',
            field=models.DateField(null=True, blank=True),
        ),
    ]
