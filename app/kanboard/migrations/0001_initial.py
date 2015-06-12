# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0002_auto_20150610_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True)),
                ('company', models.ForeignKey(related_name='board', verbose_name=b'company', to='company.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('order', models.SmallIntegerField()),
                ('backlogged_at', models.DateTimeField(default=datetime.datetime.now)),
                ('started_at', models.DateTimeField(null=True, blank=True)),
                ('done_at', models.DateTimeField(null=True, blank=True)),
                ('description', models.TextField(blank=True)),
                ('size', models.CharField(max_length=80, blank=True)),
                ('color', models.CharField(max_length=7, blank=True)),
                ('ready', models.BooleanField()),
                ('blocked', models.BooleanField()),
                ('blocked_because', models.TextField(blank=True)),
                ('board', models.ForeignKey(related_name='cards', to='kanboard.Board')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
                ('board', models.ForeignKey(related_name='phases', to='kanboard.Board')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='PhaseLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.SmallIntegerField(default=0)),
                ('date', models.DateField()),
                ('phase', models.ForeignKey(related_name='logs', to='kanboard.Phase')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='phase',
            field=models.ForeignKey(related_name='cards', to='kanboard.Phase'),
        ),
        migrations.AlterUniqueTogether(
            name='phaselog',
            unique_together=set([('phase', 'date')]),
        ),
    ]
