# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Founder',
            fields=[
                ('userprofile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='home.UserProfile')),
                ('equity', models.FloatField(default=0, blank=True)),
                ('about', models.CharField(max_length=2000, verbose_name='about', blank=True)),
                ('education', models.ForeignKey(verbose_name='Education level', blank=True, to='home.Education', null=True)),
                ('expertise', models.ManyToManyField(to='home.Expertise', verbose_name='Areas of expertise', blank=True)),
            ],
            bases=('home.userprofile',),
        ),
    ]
