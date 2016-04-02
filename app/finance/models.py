# coding: utf-8

from django.db import models
from app.company.models import Company
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _


# Grants
class Bourse(models.Model):
    name = models.CharField(
        blank=True,
        max_length=200,
        verbose_name=_('Name')
    )
    dateSoumission = models.DateField(verbose_name=_('Date of submission'))
    sommeSoumission = models.PositiveIntegerField(
        verbose_name=_('Amount requested')
    )
    dateReception = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Received date')
    )
    sommeReception = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('Amount received')
    )
    description = models.CharField(
        blank=True,
        max_length=512,
        verbose_name=_('Description')
    )
    company = models.ForeignKey(
        Company,
        verbose_name=_('Company'),
        related_name="grants"
    )

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('finance:detail_finance', args={self.company.id})


# Subsidies
class Subvention(models.Model):
    name = models.CharField(
        blank=True,
        max_length=200,
        verbose_name=_('Name')
    )
    dateSoumission = models.DateField(
        verbose_name=_('Date of submission')
    )
    sommeSoumission = models.PositiveIntegerField(
        verbose_name=_('Amount requested')
    )
    dateReception = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Received date')
    )
    sommeReception = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('Amount received')
    )
    description = models.CharField(
        blank=True,
        max_length=512,
        verbose_name=_('Description')
    )
    company = models.ForeignKey(
        Company,
        verbose_name=_('Company'),
        related_name="subsidies"
    )

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('finance:detail_finance', args={self.company.id})


# Investments
class Investissement(models.Model):
    name = models.CharField(
        blank=True,
        max_length=200,
        verbose_name=_('Name')
    )
    dateSoumission = models.DateField(
        verbose_name=_('Date of submission')
    )
    sommeSoumission = models.PositiveIntegerField(
        verbose_name=_('Amount requested')
    )
    dateReception = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Received date')
    )
    sommeReception = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('Amount received')
    )
    description = models.CharField(
        blank=True,
        max_length=512,
        verbose_name=_('Description')
    )
    company = models.ForeignKey(
        Company,
        verbose_name=_('Company'),
        related_name="investments"
    )

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('finance:detail_finance', args={self.company.id})


# Loans
class Pret(models.Model):
    name = models.CharField(
        blank=True,
        max_length=200,
        verbose_name=_('Name')
    )
    dateSoumission = models.DateField(
        verbose_name=_('Date of submission')
    )
    sommeSoumission = models.PositiveIntegerField(
        verbose_name=_('Amount requested')
    )
    dateReception = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Received date')
    )
    sommeReception = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('Amount received')
    )
    description = models.CharField(
        blank=True,
        max_length=512,
        verbose_name=_('Description')
    )
    company = models.ForeignKey(
        Company,
        verbose_name=_('Company'),
        related_name="loans"
    )

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('finance:detail_finance', args={self.company.id})


# Sales
class Vente(models.Model):
    name = models.CharField(
        blank=True,
        max_length=200,
        verbose_name=_('Name')
    )
    dateSoumission = models.DateField(
        verbose_name=_('Date of submission')
    )
    sommeSoumission = models.PositiveIntegerField(
        verbose_name=_('Amount requested')
    )
    dateReception = models.DateField(
        blank=True,
        null=True,
        verbose_name=_('Received date')
    )
    sommeReception = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('Amount received')
    )
    description = models.CharField(
        blank=True,
        max_length=512,
        verbose_name=_('Description')
    )
    company = models.ForeignKey(
        Company,
        verbose_name=_('Company'),
        related_name="sales"
    )

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('finance:detail_finance', args={self.company.id})
