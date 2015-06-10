# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='education',
            field=models.CharField(max_length=200, verbose_name='Education level'),
        ),
        migrations.AlterField(
            model_name='expertise',
            name='expertise',
            field=models.CharField(max_length=200, verbose_name='Area of expertise'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Phone', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to=b'user_profile', verbose_name='Picture', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(related_name='profile', verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userProfile_id',
            field=models.AutoField(serialize=False, verbose_name='Identifiant', primary_key=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.URLField(verbose_name='Web site', blank=True),
        ),
    ]
