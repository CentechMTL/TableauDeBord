# coding: utf-8

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    first_name = forms.CharField(
        label=_('First name'),
        required=True,
    )
    first_name.widget.attrs.update({'placeholder': _(u'First name')})

    last_name = forms.CharField(
        label=_('Last name'),
        required=True,
    )
    last_name.widget.attrs.update({'placeholder': _(u'Last name')})

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
