# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('dateSoumission', models.DateField()),
                ('sommeSoumission', models.PositiveIntegerField()),
                ('dateReception', models.DateField(null=True, blank=True)),
                ('sommeReception', models.PositiveIntegerField(null=True, blank=True)),
                ('description', models.CharField(max_length=512, blank=True)),
                ('company', models.ForeignKey(to='company.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Investissement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('dateSoumission', models.DateField()),
                ('sommeSoumission', models.PositiveIntegerField()),
                ('dateReception', models.DateField(null=True, blank=True)),
                ('sommeReception', models.PositiveIntegerField(null=True, blank=True)),
                ('description', models.CharField(max_length=512, blank=True)),
                ('company', models.ForeignKey(to='company.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Pret',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('dateSoumission', models.DateField()),
                ('sommeSoumission', models.PositiveIntegerField()),
                ('dateReception', models.DateField(null=True, blank=True)),
                ('sommeReception', models.PositiveIntegerField(null=True, blank=True)),
                ('description', models.CharField(max_length=512, blank=True)),
                ('company', models.ForeignKey(to='company.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Subvention',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('dateSoumission', models.DateField()),
                ('sommeSoumission', models.PositiveIntegerField()),
                ('dateReception', models.DateField(null=True, blank=True)),
                ('sommeReception', models.PositiveIntegerField(null=True, blank=True)),
                ('description', models.CharField(max_length=512, blank=True)),
                ('company', models.ForeignKey(to='company.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, blank=True)),
                ('dateSoumission', models.DateField()),
                ('sommeSoumission', models.PositiveIntegerField()),
                ('dateReception', models.DateField(null=True, blank=True)),
                ('sommeReception', models.PositiveIntegerField(null=True, blank=True)),
                ('description', models.CharField(max_length=512, blank=True)),
                ('company', models.ForeignKey(to='company.Company')),
            ],
        ),
    ]
