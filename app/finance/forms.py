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

class FinanceCreateForm(forms.Form):
    name = forms.CharField(
        label=_('Name'),
        required=True,
    )

    sommeSoumission = forms.DecimalField(
        label=_('Amount requested'),
        required=True,
        min_value = 0,
    )

    dateSoumission = forms.DateField(
        label=_('Date of submission'),
        input_formats=('%Y-%m-%d',),
    )
    dateSoumission.widget.attrs.update({'type': 'date', 'class': 'datepicker'})

    sommeReception = forms.DecimalField(
        label=_('Amount received'),
        required=True,
        min_value = 0,
    )

    dateReception = forms.DateField(
        label=_('Date de reception'),
        required = False,
        input_formats=('%Y-%m-%d',),
    )
    dateReception.widget.attrs.update({'type': 'date', 'class': 'datepicker'})

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

    def __init__(self, *args, **kwargs):
        super(FinanceCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'content-wrapper'
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Field('name'),
            Field('sommeSoumission'),
            Field('dateSoumission'),
            Field('sommeReception'),
            Field('dateReception'),
            Field('description'),
            StrictButton(_('Save'), type="submit")
        )

class FinanceForm(forms.Form):
    name = forms.CharField(
        label=_('Name'),
        required=True,
    )

    sommeSoumission = forms.DecimalField(
        label=_('Amount requested'),
        required=True,
        min_value = 0,
    )

    dateSoumission = forms.DateField(
        label=_('Date of submission'),
        input_formats=('%Y-%m-%d',),
    )
    dateSoumission.widget.attrs.update({'type': 'date', 'class': 'datepicker'})

    sommeReception = forms.DecimalField(
        label=_('Amount received'),
        required=True,
        min_value = 0,
    )

    dateReception = forms.DateField(
        label=_('Date de reception'),
        required = False,
        input_formats=('%Y-%m-%d',),
    )
    dateReception.widget.attrs.update({'type': 'date', 'class': 'datepicker'})

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

    def __init__(self, object, *args, **kwargs):
        super(FinanceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'content-wrapper'
        self.helper.form_method = 'post'

        self.object = object
        self.fields['name'].initial = object.name
        self.fields['sommeSoumission'].initial = object.sommeSoumission
        self.fields['dateSoumission'].initial = object.dateSoumission.isoformat()
        self.fields['sommeReception'].initial = object.sommeReception
        if(object.dateReception):
            self.fields['dateReception'].initial = object.dateReception.isoformat()
        self.fields['description'].initial = object.description

        self.helper.layout = Layout(
            Field('name'),
            Field('sommeSoumission'),
            Field('dateSoumission'),
            Field('sommeReception'),
            Field('dateReception'),
            Field('description'),
            StrictButton(_('Save'), type="submit")
        )

    def save(self):
        self.object.save()