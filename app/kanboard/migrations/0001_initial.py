# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20150610_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('comment', models.TextField(blank=True)),
                ('order', models.SmallIntegerField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('order', models.SmallIntegerField()),
                ('status', models.CharField(default=b'progress', max_length=25, choices=[(b'upcoming', b'Upcoming'), (b'progress', b'In progress'), (b'finished', b'Finished')])),
                ('description', models.TextField(blank=True)),
                ('limit', models.SmallIntegerField(null=True, blank=True)),
                ('company', models.ForeignKey(related_name='phases', to='company.Company')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='card',
            name='phase',
            field=models.ForeignKey(related_name='cards', to='kanboard.Phase'),
        ),
    ]
