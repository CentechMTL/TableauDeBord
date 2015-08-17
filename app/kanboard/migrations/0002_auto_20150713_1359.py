# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('kanboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='state',
            field=models.BooleanField(default=None, verbose_name='State'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='card',
            name='assigned',
            field=models.ForeignKey(related_name='cards_assigned', blank=True, to='founder.Founder', null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='creator',
            field=models.ForeignKey(related_name='cards_create', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='phase',
            field=models.CharField(max_length=50, verbose_name='Phase', choices=[(1, 'Finance'), (2, 'R&D'), (3, 'Centech')]),
        ),
    ]
