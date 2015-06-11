# coding: utf-8

from django import forms
import django_filters
from app.founder.models import Founder
from app.home.models import Expertise, Education

from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, \
    Submit, Field, ButtonHolder, Hidden, Div

from django.utils.translation import ugettext_lazy as _

class FounderFilter(django_filters.FilterSet):
    class Meta:
        model = Founder
        fields = ['expertise']

class FounderCreateForm(forms.Form):

    firstname = forms.CharField(
        label=_('First name'),
        required=True,
    )
    firstname.widget.attrs.update({'placeholder': _(u'First name')})

    lastname = forms.CharField(
        label=_('Last name'),
        required=True,
    )
    lastname.widget.attrs.update({'placeholder': _(u'Last name')})

    username = forms.CharField(
        label=_('Username'),
        required=True,
    )
    username.widget.attrs.update({'placeholder': _(u'Username')})

    email = forms.CharField(
        label=_('Email'),
        required=True,
    )
    email.widget.attrs.update({'placeholder': _(u'Email')})

    phone = forms.CharField(
        label=_('Phone number'),
        required=False,
        max_length=10
    )
    phone.widget.attrs.update({'placeholder': _(u'Phone number')})

    website = forms.URLField(
        label=_('Web site'),
        required=False,
    )
    website.widget.attrs.update({'placeholder': _(u'https://example.com')})

    about = forms.CharField(
        label=_('Description'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': _(u'Write here a brief summary of your skills and your career.'),
                'class': 'md-editor'
            }
        )
    )

    education = forms.ModelChoiceField(
        label=_(u"Education"),
        queryset=Education.objects.all(),
        required=False,
        empty_label=None
    )

    expertise = forms.ModelMultipleChoiceField(
        label=_(u"Areas of expertise"),
        queryset=Expertise.objects.all(),
        required=False,
        widget=forms.SelectMultiple()
    )

    picture = forms.ImageField(
        label=_(u'Picture'),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(FounderCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'content-wrapper'
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            HTML("<h1>"),
            HTML(_("New founder")),
            HTML("</h1>"),
            Field('firstname'),
            Field('lastname'),
            Field('username'),
            Field('email'),
            Field('picture'),
            Field('phone'),
            Field('website'),
            Field('education'),
            Field('expertise'),
            HTML(_(u"""Use the Ctrl key on your keyboard to select multiple. <br> If it lacks a domain that you would like to add to this list, do not hesitate to talk to the team Centech""")),
            Field('about'),
            StrictButton(_('Save'), type="submit")
        )

class FounderUpdateForm(forms.Form):

    firstname = forms.CharField(
        label=_('First name'),
        required=True,
    )
    firstname.widget.attrs.update({'placeholder': _(u'First name')})

    lastname = forms.CharField(
        label=_('Last name'),
        required=True,
    )
    lastname.widget.attrs.update({'placeholder': _(u'Last name')})

    phone = forms.CharField(
        label=_('Phone number'),
        required=False,
        max_length=10
    )
    phone.widget.attrs.update({'placeholder': _(u'Phone number')})

    website = forms.URLField(
        label=_('Web site'),
        required=False,
    )
    website.widget.attrs.update({'placeholder': _(u'https://example.com')})

    about = forms.CharField(
        label=_('Description'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': _(u'Write here a brief summary of your skills and your career.'),
                'class': 'md-editor'
            }
        )
    )

    education = forms.ModelChoiceField(
        label=_(u"Education"),
        queryset=Education.objects.all(),
        required=False,
        empty_label=None
    )

    expertise = forms.ModelMultipleChoiceField(
        label=_(u"Areas of expertise"),
        queryset=Expertise.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                'required': 'required',
            }
        )
    )

    picture = forms.ImageField(
        label=_(u'Picture'),
        required=False,
    )

    def __init__(self, founder, *args, **kwargs):
        super(FounderUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'content-wrapper'
        self.helper.form_method = 'post'

        self.founder = founder
        self.fields['about'].initial = founder.about
        self.fields['education'].initial = founder.education
        self.fields['expertise'].initial = founder.expertise.all
        self.fields['firstname'].initial = founder.user.first_name
        self.fields['lastname'].initial = founder.user.last_name
        self.fields['website'].initial = founder.website
        self.fields['phone'].initial = founder.phone

        self.helper.layout = Layout(
            HTML("<h1>"),
            HTML(_("Update this founder")),
            HTML("</h1>"),
            Field('firstname'),
            Field('lastname'),
            Field('picture'),
            Field('phone'),
            Field('website'),
            Field('education'),
            Field('expertise'),
            HTML(_(u"""Use the Ctrl key on your keyboard to select multiple. <br> If it lacks a domain that you would like to add to this list, do not hesitate to talk to the team Centech""")),
            Field('about'),
            StrictButton(_('Save'), type="submit")
        )

    def save(self):
        self.founder.save()
        self.founder.user.save()