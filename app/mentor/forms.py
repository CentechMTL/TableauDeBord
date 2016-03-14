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
FILTER_MENTOR_CHOICES.insert(0, ('', '---------'))


class MentorFilter(FilterSet):
    name = MethodFilter(action='filter_username', label=_('Search by name'))
    type = ChoiceFilter(choices=FILTER_MENTOR_CHOICES)

    class Meta:
        model = Mentor
        fields = {
            'expertise': ['exact'],
            'type': ['exact']
        }

    def filter_username(self, queryset, value):
        if value:
            query = []

            value = re.sub("[^\w]", " ",  value).split()
            for word in value:

                firstname = list(
                    queryset.filter(
                        user__first_name__icontains=word
                    ).all()
                )

                lastname = list(
                    queryset.filter(
                        user__last_name__icontains=word
                    ).all()
                )

                username = list(
                    queryset.filter(
                        user__username__icontains=word
                    ).all()
                )

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


class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = [
            'type',
            'url',
            'picture',
            'about',
            'expertise',
            'phone',
            'website',
            'facebook',
            'twitter',
            'googlePlus',
            'linkedIn'
        ]

    type = forms.ChoiceField(
        choices=MENTOR_TYPE_CHOICES,
    )

    url = forms.URLField(
        label=_('Directory of ETS'),
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
    linkedIn.widget.attrs.update(
        {
            'placeholder': _(u'https://ca.linkedin.com/in/username')
        }
    )

    phone = forms.CharField(
        label=_('Phone number'),
        required=False,
        max_length=10
    )
    phone.widget.attrs.update(
        {
            'placeholder': _(u'Phone number')
        }
    )

    website = forms.URLField(
        label=_('Web site'),
        required=False,
    )
    website.widget.attrs.update(
        {
            'placeholder': _(u'https://example.com')
        }
    )

    about = forms.CharField(
        label=_('Description'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': _(u'Write here a brief summary of your skills '
                                 u'and your career.'),
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
