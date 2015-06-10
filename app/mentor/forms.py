# coding: utf-8

from django import forms
import django_filters
from app.mentor.models import Mentor
from app.home.models import Expertise, Education

from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, \
    Submit, Field, ButtonHolder, Hidden, Div

from django.utils.translation import ugettext_lazy as _

class MentorFilter(django_filters.FilterSet):
    class Meta:
        model = Mentor
        fields = ['expertise']

class MentorCreateForm(forms.Form):

    firstname = forms.CharField(
        label=_('First name'),
        required=False,
    )
    firstname.widget.attrs.update({'placeholder': _(u'First name')})

    lastname = forms.CharField(
        label=_('Last name'),
        required=False,
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
        label=_('Picture'),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(MentorCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'content-wrapper'
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            HTML("<h1>"),
            HTML(_("New mentor")),
            HTML("</h1>"),
            Field('firstname'),
            Field('lastname'),
            Field('username'),
            Field('email'),
            Field('picture'),
            Field('phone'),
            Field('website'),
            Field('expertise'),
            HTML(_(u"""Use the Ctrl key on your keyboard to select multiple. <br> If it lacks a domain that you would like to add to this list, do not hesitate to talk to the team Centech""")),
            Field('about'),
            StrictButton(_('Save'), type="submit")
        )

class MentorUpdateForm(forms.Form):

    firstname = forms.CharField(
        label=_('First name'),
        required=False,
    )
    firstname.widget.attrs.update({'placeholder': _(u'First name')})

    lastname = forms.CharField(
        label=_('Last name'),
        required=False,
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
        label=_('Picture'),
        required=False,
    )

    def __init__(self, mentor, *args, **kwargs):
        super(MentorUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'content-wrapper'
        self.helper.form_method = 'post'

        self.mentor = mentor
        self.fields['about'].initial = mentor.about
        self.fields['expertise'].initial = mentor.expertise.all
        self.fields['firstname'].initial = mentor.user.first_name
        self.fields['lastname'].initial = mentor.user.last_name
        self.fields['phone'].initial = mentor.phone
        self.fields['website'].initial = mentor.website

        self.helper.layout = Layout(
            HTML("<h1>"),
            HTML(_("Update this mentor")),
            HTML("</h1>"),
            Field('firstname'),
            Field('lastname'),
            Field('picture'),
            Field('phone'),
            Field('website'),
            Field('expertise'),
            HTML(_(u"""Use the Ctrl key on your keyboard to select multiple. <br> If it lacks a domain that you would like to add to this list, do not hesitate to talk to the team Centech""")),
            Field('about'),
            StrictButton(_('Save'), type="submit")
        )

    def save(self):
        self.mentor.save()
        self.mentor.user.save()