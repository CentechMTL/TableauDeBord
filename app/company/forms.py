# coding: utf-8

import django_filters
from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, \
    Submit, Field, ButtonHolder, Hidden, Div

from app.company.models import Company, CompanyStatus, Presence
from app.founder.models import Founder
from app.mentor.models import Mentor


class CompanyFilter(django_filters.FilterSet):
    # http://django-filter.readthedocs.org/en/latest/usage.html
    class Meta:
        model = Company
        fields = {
            'companyStatus': ['exact'],
            'name': ['icontains']
        }


class PresenceForm(forms.ModelForm):
    class Meta:
        model = Presence
        fields = ['date']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'datepicker'
                }
            )
        }

    date = forms.DateField()


class CompanyStatusForm(forms.ModelForm):
    class Meta:
        model = CompanyStatus
        fields = ['status']

    status = forms.CharField(
        label=_('Name'),
        required=True,
    )
    status.widget.attrs.update({'placeholder': _(u'Name of the new status')})


class MiniCompanyStatusUpdateForm(forms.Form):
    comment = forms.CharField(
        label=_('Comment'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': _(u'Write here a comment about this group.'),
                'class': 'md-editor'
            }
        )
    )

    def __init__(self, status, *args, **kwargs):
        super(MiniCompanyStatusUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'content-wrapper'
        self.helper.form_method = 'post'

        self.status = status
        self.fields['comment'].initial = status.comment

        self.helper.layout = Layout(
            Field('comment'),
            StrictButton(_('Save'), type="submit")
        )

    def save(self):
        self.status.save()


class MiniCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name',
            'logo',
            'video',
            'url',
            'facebook',
            'googlePlus',
            'linkedIn',
            'twitter',
            'description'
        ]

    name = forms.CharField(
        label=_('Name'),
        required=True,
    )
    name.widget.attrs.update(
        {
            'placeholder': _(u'Company name')
        }
    )

    logo = forms.ImageField(
        label=_('Logo'),
        required=False,
    )

    video = forms.URLField(
        label=_('Video'),
        required=False,
    )
    video.widget.attrs.update(
        {
            'placeholder': _(u'https://urlvideo.com/')
        }
    )

    url = forms.URLField(
        label=_('Web site'),
        required=False,
    )
    url.widget.attrs.update(
        {
            'placeholder': _(u'https://example.com')
        }
    )

    facebook = forms.URLField(
        label=_('Facebook'),
        required=False,
    )
    facebook.widget.attrs.update(
        {
            'placeholder': _(u'https://www.facebook.com/lastname.firstname')
        }
    )

    twitter = forms.URLField(
        label=_('Twitter'),
        required=False,
    )
    twitter.widget.attrs.update(
        {
            'placeholder': _(u'https://twitter.com/username')
        }
    )

    googlePlus = forms.URLField(
        label=_('Google+'),
        required=False,
    )
    googlePlus.widget.attrs.update(
        {
            'placeholder': _(u'https://plus.google.com/id')
        }
    )

    linkedIn = forms.URLField(
        label=_('linkedIn'),
        required=False,
    )
    linkedIn.widget.attrs.update({'placeholder': _(u'https://ca.linkedin.com'
                                                   u'/in/username')})

    description = forms.CharField(
        label=_('Description'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': _(u'Write here a brief summary '
                                 u'of your business.'),
                'class': 'md-editor'
            }
        )
    )


class CompanyForm(MiniCompanyForm):
    class Meta:
        model = Company
        fields = [
            'name',
            'companyStatus',
            'incubated_on',
            'endOfIncubation',
            'logo',
            'video',
            'url',
            'facebook',
            'googlePlus',
            'linkedIn',
            'twitter',
            'description',
            'founders',
            'mentors'
        ]

    companyStatus = forms.ModelChoiceField(
        label=_(u"Incubation phase"),
        queryset=CompanyStatus.objects.all(),
        required=True,
    )

    incubated_on = forms.DateField(
        label=_('Start date'),
        required=False,
        input_formats=('%Y-%m-%d',),
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'datepicker'
            }
        )
    )

    endOfIncubation = forms.DateField(
        label=_('End date'),
        required=False,
        input_formats=('%Y-%m-%d',),
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'datepicker'
            }
        )
    )

    founders = forms.ModelMultipleChoiceField(
        label=_(u"Founders"),
        queryset=Founder.objects.all(),
        required=False,
        widget=forms.SelectMultiple()
    )

    mentors = forms.ModelMultipleChoiceField(
        label=_(u"Mentors"),
        queryset=Mentor.objects.all(),
        required=False,
        widget=forms.SelectMultiple()
    )
