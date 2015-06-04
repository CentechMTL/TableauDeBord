# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('education', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Education',
            },
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expertise', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Expertise',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('userProfile_id', models.AutoField(serialize=False, primary_key=True)),
                ('phone', models.CharField(max_length=10, verbose_name='phone', blank=True)),
                ('website', models.URLField(verbose_name='web site', blank=True)),
                ('picture', models.ImageField(upload_to=b'user_profile', verbose_name='personal photograph', blank=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
