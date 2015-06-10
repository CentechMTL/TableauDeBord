# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bourse',
            name='company',
            field=models.ForeignKey(verbose_name='Company', to='company.Company'),
        ),
        migrations.AlterField(
            model_name='bourse',
            name='dateReception',
            field=models.DateField(null=True, verbose_name='Received date', blank=True),
        ),
        migrations.AlterField(
            model_name='bourse',
            name='dateSoumission',
            field=models.DateField(verbose_name='Date of submission'),
        ),
        migrations.AlterField(
            model_name='bourse',
            name='description',
            field=models.CharField(max_length=512, verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='bourse',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name', blank=True),
        ),
        migrations.AlterField(
            model_name='bourse',
            name='sommeReception',
            field=models.PositiveIntegerField(null=True, verbose_name='Amount received', blank=True),
        ),
        migrations.AlterField(
            model_name='bourse',
            name='sommeSoumission',
            field=models.PositiveIntegerField(verbose_name='Amount requested'),
        ),
        migrations.AlterField(
            model_name='investissement',
            name='company',
            field=models.ForeignKey(verbose_name='Company', to='company.Company'),
        ),
        migrations.AlterField(
            model_name='investissement',
            name='dateReception',
            field=models.DateField(null=True, verbose_name='Received date', blank=True),
        ),
        migrations.AlterField(
            model_name='investissement',
            name='dateSoumission',
            field=models.DateField(verbose_name='Date of submission'),
        ),
        migrations.AlterField(
            model_name='investissement',
            name='description',
            field=models.CharField(max_length=512, verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='investissement',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name', blank=True),
        ),
        migrations.AlterField(
            model_name='investissement',
            name='sommeReception',
            field=models.PositiveIntegerField(null=True, verbose_name='Amount received', blank=True),
        ),
        migrations.AlterField(
            model_name='investissement',
            name='sommeSoumission',
            field=models.PositiveIntegerField(verbose_name='Amount requested'),
        ),
        migrations.AlterField(
            model_name='pret',
            name='company',
            field=models.ForeignKey(verbose_name='Company', to='company.Company'),
        ),
        migrations.AlterField(
            model_name='pret',
            name='dateReception',
            field=models.DateField(null=True, verbose_name='Received date', blank=True),
        ),
        migrations.AlterField(
            model_name='pret',
            name='dateSoumission',
            field=models.DateField(verbose_name='Date of submission'),
        ),
        migrations.AlterField(
            model_name='pret',
            name='description',
            field=models.CharField(max_length=512, verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='pret',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name', blank=True),
        ),
        migrations.AlterField(
            model_name='pret',
            name='sommeReception',
            field=models.PositiveIntegerField(null=True, verbose_name='Amount received', blank=True),
        ),
        migrations.AlterField(
            model_name='pret',
            name='sommeSoumission',
            field=models.PositiveIntegerField(verbose_name='Amount requested'),
        ),
        migrations.AlterField(
            model_name='subvention',
            name='company',
            field=models.ForeignKey(verbose_name='Company', to='company.Company'),
        ),
        migrations.AlterField(
            model_name='subvention',
            name='dateReception',
            field=models.DateField(null=True, verbose_name='Received date', blank=True),
        ),
        migrations.AlterField(
            model_name='subvention',
            name='dateSoumission',
            field=models.DateField(verbose_name='Date of submission'),
        ),
        migrations.AlterField(
            model_name='subvention',
            name='description',
            field=models.CharField(max_length=512, verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='subvention',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name', blank=True),
        ),
        migrations.AlterField(
            model_name='subvention',
            name='sommeReception',
            field=models.PositiveIntegerField(null=True, verbose_name='Amount received', blank=True),
        ),
        migrations.AlterField(
            model_name='subvention',
            name='sommeSoumission',
            field=models.PositiveIntegerField(verbose_name='Amount requested'),
        ),
        migrations.AlterField(
            model_name='vente',
            name='company',
            field=models.ForeignKey(verbose_name='Company', to='company.Company'),
        ),
        migrations.AlterField(
            model_name='vente',
            name='dateReception',
            field=models.DateField(null=True, verbose_name='Received date', blank=True),
        ),
        migrations.AlterField(
            model_name='vente',
            name='dateSoumission',
            field=models.DateField(verbose_name='Date of submission'),
        ),
        migrations.AlterField(
            model_name='vente',
            name='description',
            field=models.CharField(max_length=512, verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='vente',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name', blank=True),
        ),
        migrations.AlterField(
            model_name='vente',
            name='sommeReception',
            field=models.PositiveIntegerField(null=True, verbose_name='Amount received', blank=True),
        ),
        migrations.AlterField(
            model_name='vente',
            name='sommeSoumission',
            field=models.PositiveIntegerField(verbose_name='Amount requested'),
        ),
    ]
