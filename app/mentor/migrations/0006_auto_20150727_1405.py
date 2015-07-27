# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0005_mentor_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='type',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Type', choices=[('1', b'Affaires'), ('2', b'Technologiques')]),
        ),
    ]
