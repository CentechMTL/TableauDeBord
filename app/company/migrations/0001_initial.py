# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0001_initial'),
        ('founder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to=b'logo', blank=True)),
                ('url', models.URLField(blank=True)),
                ('video', embed_video.fields.EmbedVideoField(blank=True)),
                ('description', models.TextField(max_length=2000, blank=True)),
                ('created', models.DateTimeField(blank=True)),
                ('updated', models.DateTimeField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='CompanyStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Company Status',
            },
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(blank=True)),
                ('company', models.ManyToManyField(to='company.Company', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Presences',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='companyStatus',
            field=models.ForeignKey(verbose_name='Phase', to='company.CompanyStatus'),
        ),
        migrations.AddField(
            model_name='company',
            name='founders',
            field=models.ManyToManyField(to='founder.Founder', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='mentors',
            field=models.ManyToManyField(to='mentor.Mentor', blank=True),
        ),
    ]
