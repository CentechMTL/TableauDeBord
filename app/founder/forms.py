# coding: utf-8

import re

from django import forms
from django_filters import FilterSet, MethodFilter
from app.founder.models import Founder
from app.home.models import Expertise, Education

from django.utils.translation import ugettext_lazy as _


class FounderFilter(FilterSet):
    name = MethodFilter(
        action='filter_username',
        label=_('Search by name')
    )

    class Meta:
        model = Founder
        fields = ['expertise']

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


class FounderForm(forms.ModelForm):
    class Meta:
        model = Founder
        fields = [
            'picture',
            'education',
            'about',
            'expertise',
            'phone',
            'website',
            'facebook',
            'twitter',
            'googlePlus',
            'linkedIn'
        ]

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

    about = forms.CharField(
        label=_('Description'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': _(u'Write here a brief summary of your '
                                 u'skills and career.'),
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
