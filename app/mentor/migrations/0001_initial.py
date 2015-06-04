# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='home.UserProfile')),
                ('about', models.CharField(max_length=2000, verbose_name='About', blank=True)),
                ('expertise', models.ManyToManyField(to='home.Expertise', verbose_name='Areas of expertise')),
            ],
            bases=('home.userprofile',),
        ),
    ]
