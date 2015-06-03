# coding: utf-8

from django import forms
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import widgets
from app.finance.models import Bourse, Subvention, Investissement, Pret, Vente

class BourseForm(forms.ModelForm):
    class Meta:
        model = Bourse
        fields = ['name','dateSoumission','sommeSoumission','dateReception',
              'sommeReception']

    def __init__(self, *args, **kwargs):
        super(BourseForm, self).__init__(*args, **kwargs)
        self.fields['dateSoumission'].widget = AdminDateWidget()

#TODO Check for create a form who work for all type of finance