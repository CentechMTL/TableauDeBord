# coding: utf-8

from django import forms
from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from app.finance.models import Bourse, Subvention, Investissement, Pret, Vente

from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, \
    Submit, Field, ButtonHolder, Hidden, Div

from embed_video.fields import EmbedVideoField
from django.utils.translation import ugettext_lazy as _
from django.forms import widgets


class FinanceForm(forms.ModelForm):
    name = forms.CharField(
        label=_('Name'),
        required=True,
    )

    sommeSoumission = forms.DecimalField(
        label=_('Amount requested'),
        required=True,
        min_value=0,
    )

    dateSoumission = forms.DateField(
        label=_('Date of submission'),
        input_formats=('%Y-%m-%d',),
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'datepicker'
            }
        )
    )
    dateSoumission.widget.attrs.update(
        {
            'type': 'date',
            'class': 'datepicker'
        }
    )

    sommeReception = forms.DecimalField(
        label=_('Amount received'),
        required=False,
        min_value=0,
    )

    dateReception = forms.DateField(
        label=_('Date de reception'),
        required=False,
        input_formats=('%Y-%m-%d',),
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'datepicker'
            }
        )
    )
    dateReception.widget.attrs.update(
        {
            'type': 'date',
            'class': 'datepicker'
        }
    )

    description = forms.CharField(
        label=_('Description'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': _(u'Write here a brief description.'),
                'class': 'md-editor'
            }
        )
    )


class BourseForm(FinanceForm):
    class Meta:
        model = Bourse
        fields = [
            'name',
            'sommeSoumission',
            'dateSoumission',
            'sommeReception',
            'dateReception',
            'description'
        ]


class SubventionForm(FinanceForm):
    class Meta:
        model = Subvention
        fields = [
            'name',
            'sommeSoumission',
            'dateSoumission',
            'sommeReception',
            'dateReception',
            'description'
        ]


class PretForm(FinanceForm):
    class Meta:
        model = Pret
        fields = [
            'name',
            'sommeSoumission',
            'dateSoumission',
            'sommeReception',
            'dateReception',
            'description'
        ]


class InvestissementForm(FinanceForm):
    class Meta:
        model = Investissement
        fields = [
            'name',
            'sommeSoumission',
            'dateSoumission',
            'sommeReception',
            'dateReception',
            'description'
        ]


class VenteForm(FinanceForm):
    class Meta:
        model = Vente
        fields = [
            'name',
            'sommeSoumission',
            'dateSoumission',
            'sommeReception',
            'dateReception',
            'description'
        ]
