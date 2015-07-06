# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0003_mentor_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='type',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Type', choices=[('1', b'Finance'), ('2', b'Technologie')]),
        ),
    ]
