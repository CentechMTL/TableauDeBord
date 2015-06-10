# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='companyStatus',
            field=models.ForeignKey(verbose_name='Status', to='company.CompanyStatus'),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='founders',
            field=models.ManyToManyField(to='founder.Founder', verbose_name='Founders', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to=b'logo', verbose_name='Logo', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='mentors',
            field=models.ManyToManyField(to='mentor.Mentor', verbose_name='Mentors', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='company',
            name='url',
            field=models.URLField(verbose_name='URL', blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='video',
            field=embed_video.fields.EmbedVideoField(verbose_name='Video', blank=True),
        ),
        migrations.AlterField(
            model_name='companystatus',
            name='status',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='presence',
            name='company',
            field=models.ManyToManyField(to='company.Company', verbose_name='Companies', blank=True),
        ),
        migrations.AlterField(
            model_name='presence',
            name='date',
            field=models.DateTimeField(verbose_name='Date', blank=True),
        ),
    ]
