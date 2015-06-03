# coding: utf-8

from django import forms
import django_filters
from app.company.models import Company, CompanyStatus
from app.founder.models import Founder
from app.mentor.models import Mentor
from django.contrib.admin.widgets import AdminDateWidget
from django.db import models

from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, \
    Submit, Field, ButtonHolder, Hidden, Div

from embed_video.fields import EmbedVideoField

#http://django-filter.readthedocs.org/en/latest/usage.html
class CompanyFilter(django_filters.FilterSet):
    class Meta:
        model = Company
        fields = ['companyStatus']

class CompanyCreateForm(forms.Form):

    name = forms.CharField(
        label=('Name'),
        required=True,
    )
    name.widget.attrs.update({'placeholder': (u'Name of the company')})

    logo = forms.ImageField(
        label=('Logo'),
        required=False,
    )

    video = forms.URLField(
        label=('Vidéo'),
        required=False,

    )
    video.widget.attrs.update({'placeholder': (u'https://urlvideo.com/')})

    url = forms.URLField(
        label=('Web site'),
        required=False,
    )
    url.widget.attrs.update({'placeholder': (u'https://example.com')})

    about = forms.CharField(
        label=('Description'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': (u'Rentrez ici un bref résumé de votre entreprise.'),
                'class': 'md-editor'
            }
        )
    )

    status = forms.ModelChoiceField(
        label=(u"Phase d'incubation"),
        queryset=CompanyStatus.objects.all(),
        required=True,
    )

    founders = forms.ModelMultipleChoiceField(
        label=(u"Fondateurs"),
        queryset=Founder.objects.all(),
        required=True,
        widget=forms.SelectMultiple(
            attrs={
                'required': 'required',
            }
        )
    )

    mentors = forms.ModelMultipleChoiceField(
        label=(u"Mentors"),
        queryset=Mentor.objects.all(),
        required=False,
        widget=forms.SelectMultiple()
    )

    def __init__(self, *args, **kwargs):
        super(CompanyCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'content-wrapper'
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Field('name'),
            Field('status'),
            Field('logo'),
            Field('video'),
            Field('url'),
            Field('about'),
            Field('founders'),
            Field('mentors'),
            StrictButton('Enregistrer', type="submit")
        )

class CompanyUpdateForm(forms.Form):

    name = forms.CharField(
        label=('Name'),
        required=True,
    )
    name.widget.attrs.update({'placeholder': (u'Name of the company')})

    logo = forms.ImageField(
        label=('Logo'),
        required=False,
    )

    video = forms.URLField(
        label=('Vidéo'),
        required=False,

    )

    url = forms.URLField(
        label=('Web site'),
        required=False,
    )
    url.widget.attrs.update({'placeholder': (u'https://example.com')})

    about = forms.CharField(
        label=('Description'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': (u'Rentrez ici un bref résumé de votre entreprise.'),
                'class': 'md-editor'
            }
        )
    )

    def __init__(self, company, *args, **kwargs):
        super(CompanyUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'content-wrapper'
        self.helper.form_method = 'post'

        self.company = company
        self.fields['about'].initial = company.description
        self.fields['name'].initial = company.name
        self.fields['url'].initial = company.url
        self.fields['video'].initial = company.video

        self.helper.layout = Layout(
            Field('name'),
            Field('logo'),
            Field('video'),
            Field('url'),
            Field('about'),
            StrictButton('Enregistrer', type="submit")
        )

    def save(self):
        self.company.save()