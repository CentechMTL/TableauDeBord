# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('founder', '0002_auto_20150610_1511'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0004_company_incubated_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80)),
                ('comment', models.TextField(blank=True)),
                ('deadline', models.DateField(null=True, blank=True)),
                ('phase', models.CharField(max_length=50, verbose_name='Phase', choices=[(b'Finance', 1), (b'R&D', 2), (b'Centech', 3)])),
                ('order', models.SmallIntegerField()),
                ('created', models.DateTimeField(blank=True)),
                ('updated', models.DateTimeField(blank=True)),
                ('assigned', models.ForeignKey(related_name='cards', blank=True, to='founder.Founder', null=True)),
                ('company', models.ForeignKey(related_name='cards', to='company.Company')),
                ('creator', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
