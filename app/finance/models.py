from django.db import models
from app.company.models import Company
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy

#Stock exchange
class Bourse(models.Model):
    name = models.CharField(blank=True, max_length=200)
    dateSoumission = models.DateField()
    sommeSoumission = models.PositiveIntegerField()
    dateReception = models.DateField(blank=True, null=True)
    sommeReception = models.PositiveIntegerField(blank=True, null=True)
    description = models.CharField(blank=True, max_length=512)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('detail_finance', args={self.company.id})

#Subsidies
class Subvention(models.Model):
    name = models.CharField(blank=True, max_length=200)
    dateSoumission = models.DateField()
    sommeSoumission = models.PositiveIntegerField()
    dateReception = models.DateField(blank=True, null=True)
    sommeReception = models.PositiveIntegerField(blank=True, null=True)
    description = models.CharField(blank=True, max_length=512)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('detail_finance', args={self.company.id})

#Investments
class Investissement(models.Model):
    name = models.CharField(blank=True, max_length=200)
    dateSoumission = models.DateField()
    sommeSoumission = models.PositiveIntegerField()
    dateReception = models.DateField(blank=True, null=True)
    sommeReception = models.PositiveIntegerField(blank=True, null=True)
    description = models.CharField(blank=True, max_length=512)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('detail_finance', args={self.company.id})

#Loans
class Pret(models.Model):
    name = models.CharField(blank=True, max_length=200)
    dateSoumission = models.DateField()
    sommeSoumission = models.PositiveIntegerField()
    dateReception = models.DateField(blank=True, null=True)
    sommeReception = models.PositiveIntegerField(blank=True, null=True)
    description = models.CharField(blank=True, max_length=512)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('detail_finance', args={self.company.id})

#Sales
class Vente(models.Model):
    name = models.CharField(blank=True, max_length=200)
    dateSoumission = models.DateField()
    sommeSoumission = models.PositiveIntegerField()
    dateReception = models.DateField(blank=True, null=True)
    sommeReception = models.PositiveIntegerField(blank=True, null=True)
    description = models.CharField(blank=True, max_length=512)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('detail_finance', args={self.company.id})