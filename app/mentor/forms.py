# coding: utf-8

import re

from django import forms
from django_filters import FilterSet, MethodFilter, ChoiceFilter
from app.mentor.models import Mentor, MENTOR_TYPE_CHOICES
from app.home.models import Expertise, Education

from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, \
    Submit, Field, ButtonHolder, Hidden, Div

from django.utils.translation import ugettext_lazy as _

FILTER_MENTOR_CHOICES = list(MENTOR_TYPE_CHOICES)
FILTER_MENTOR_CHOICES.insert(0, ('','---------') )

class MentorFilter(FilterSet):
    name = MethodFilter(action='filter_username')
    type = ChoiceFilter(choices= FILTER_MENTOR_CHOICES )

    class Meta:
        model = Mentor
        fields = {'expertise' : ['exact'], 'type': ['exact']}

    def filter_username(self, queryset, value):
        if value:
            query = []

            value = re.sub("[^\w]", " ",  value).split()
            for word in value:
                firstname = list(queryset.filter(user__first_name__icontains = word).all())
                lastname = list(queryset.filter(user__last_name__icontains = word).all())
                username = list(queryset.filter(user__username__icontains = word).all())

                for user in firstname:
                    if user not in query:
                        query.append(user)
                for user in lastname:
                    if user not in query:
                        query.append(user)
                for user in username:
                    if user not in query:
                        query.append(user)

            return query

        else:
            return queryset

class MentorCreateForm(forms.Form):

    type = forms.ChoiceField(
        choices = MENTOR_TYPE_CHOICES,
    )

    url = forms.URLField(
        label=_('Directory of ETS'),
        required=False,
    )
    url.widget.attrs.update({'placeholder': _(u'https://example.com')})

    facebook = forms.URLField(
        label=_('Facebook'),
        required=False,
    )
    facebook.widget.attrs.update({'placeholder': _(u'https://www.facebook.com/lastname.firstname')})

    twitter = forms.URLField(
        label=_('Twitter'),
        required=False,
    )
    twitter.widget.attrs.update({'placeholder': _(u'https://twitter.com/username')})

    googlePlus = forms.URLField(
        label=_('Google+'),
        required=False,
    )
    googlePlus.widget.attrs.update({'placeholder': _(u'https://plus.google.com/id')})

    linkedIn = forms.URLField(
        label=_('linkedIn'),
        required=False,
    )
    linkedIn.widget.attrs.update({'placeholder': _(u'https://ca.linkedin.com/in/username')})

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

    expertise = forms.ModelMultipleChoiceField(
        label=_(u"Areas of expertise"),
        queryset=Expertise.objects.all(),
        required=False,
        widget=forms.SelectMultiple()
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
            Field('url'),
            Field('facebook'),
            Field('twitter'),
            Field('googlePlus'),
            Field('linkedIn'),
            Field('type'),
            Field('expertise'),
            HTML(_(u"""Use the Ctrl key on your keyboard to select multiple. <br> If it lacks a domain that you would like to add to this list, do not hesitate to talk to the team Centech""")),
            Field('about'),
            StrictButton(_('Save'), type="submit")
        )

class MentorUpdateForm(forms.Form):

    type = forms.ChoiceField(
        choices = MENTOR_TYPE_CHOICES,
    )

    url = forms.URLField(
        label=_('Directory of ETS'),
        required=False,
    )
    url.widget.attrs.update({'placeholder': _(u'https://example.com')})

    facebook = forms.URLField(
        label=_('Facebook'),
        required=False,
    )
    facebook.widget.attrs.update({'placeholder': _(u'https://www.facebook.com/lastname.firstname')})

    twitter = forms.URLField(
        label=_('Twitter'),
        required=False,
    )
    twitter.widget.attrs.update({'placeholder': _(u'https://twitter.com/username')})

    googlePlus = forms.URLField(
        label=_('Google+'),
        required=False,
    )
    googlePlus.widget.attrs.update({'placeholder': _(u'https://plus.google.com/id')})

    linkedIn = forms.URLField(
        label=_('linkedIn'),
        required=False,
    )
    linkedIn.widget.attrs.update({'placeholder': _(u'https://ca.linkedin.com/in/username')})

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
        self.fields['facebook'].initial = mentor.facebook
        self.fields['twitter'].initial = mentor.twitter
        self.fields['googlePlus'].initial = mentor.googlePlus
        self.fields['linkedIn'].initial = mentor.linkedIn
        self.fields['type'].initial = mentor.type
        self.fields['url'].initial = mentor.url

        self.helper.layout = Layout(
            HTML("<h1>"),
            HTML(_("Update this mentor")),
            HTML("</h1>"),
            Field('firstname'),
            Field('lastname'),
            Field('picture'),
            Field('phone'),
            Field('website'),
            Field('facebook'),
            Field('twitter'),
            Field('googlePlus'),
            Field('linkedIn'),
            Field('url'),
            Field('type'),
            Field('expertise'),
            HTML(_(u"""Use the Ctrl key on your keyboard to select multiple. <br> If it lacks a domain that you would like to add to this list, do not hesitate to talk to the team Centech""")),
            Field('about'),
            StrictButton(_('Save'), type="submit")
        )

    def save(self):
        self.mentor.save()
        self.mentor.user.save()