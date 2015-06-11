# coding: utf-8

from django import forms
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import widgets
from app.finance.models import Bourse, Subvention, Investissement, Pret, Vente

class BourseForm(forms.ModelForm):
    class Meta:
        model = Bourse
        fields = ['dateSoumission', 'dateReception']
        widgets = {
            'dateSoumission' : forms.DateInput(attrs={'type':'date', 'class':'datepicker'}),
            'dateReception' : forms.DateInput(attrs={'type':'date', 'class':'datepicker'})
        }

    dateSoumission = forms.DateField()
    dateReception = forms.DateField()

class SubventionForm(forms.ModelForm):
    class Meta:
        model = Subvention
        fields = ['dateSoumission', 'dateReception']
        widgets = {
            'dateSoumission' : forms.DateInput(attrs={'type':'date', 'class':'datepicker'}),
            'dateReception' : forms.DateInput(attrs={'type':'date', 'class':'datepicker'})
        }

    dateSoumission = forms.DateField()
    dateReception = forms.DateField()

class InvestissementForm(forms.ModelForm):
    class Meta:
        model = Investissement
        fields = ['dateSoumission', 'dateReception']
        widgets = {
            'dateSoumission' : forms.DateInput(attrs={'type':'date', 'class':'datepicker'}),
            'dateReception' : forms.DateInput(attrs={'type':'date', 'class':'datepicker'})
        }

    dateSoumission = forms.DateField()
    dateReception = forms.DateField()

class PretForm(forms.ModelForm):
    class Meta:
        model = Pret
        fields = ['dateSoumission', 'dateReception']
        widgets = {
            'dateSoumission' : forms.DateInput(attrs={'type':'date', 'class':'datepicker'}),
            'dateReception' : forms.DateInput(attrs={'type':'date', 'class':'datepicker'})
        }

    dateSoumission = forms.DateField()
    dateReception = forms.DateField()

class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = ['dateSoumission', 'dateReception']
        widgets = {
            'dateSoumission' : forms.DateInput(attrs={'type':'date', 'class':'datepicker'}),
            'dateReception' : forms.DateInput(attrs={'type':'date', 'class':'datepicker'})
        }

    dateSoumission = forms.DateField()
    dateReception = forms.DateField()

#TODO Check for create a form who work for all type of finance