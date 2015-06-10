# coding: utf-8

from django import forms
from django.contrib.auth.models import User
from app.home.models import UserProfile
from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, \
    Submit, Field, ButtonHolder, Hidden, Div

from django.utils.translation import ugettext_lazy as _

# Max password length for the user.
# Unlike other fields, this is not the length of DB field
MAX_PASSWORD_LENGTH = 76
# Min password length for the user.
MIN_PASSWORD_LENGTH = 6

#TODO Faire un système d'héritage des formulaires de profil
"""
UserForm (firstname, lastname)
    ProfileForm (website, phone, picture)
        MentorForm (expertise)
        FounderForm (expertise, education)

PasswordForm (password)
"""
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class UpdatePasswordForm(forms.Form):

    password_new = forms.CharField(
        label=_(u'New password'),
        max_length=MAX_PASSWORD_LENGTH,
        min_length=MIN_PASSWORD_LENGTH,
        widget=forms.PasswordInput,
    )

    password_old = forms.CharField(
        label=_(u'Actual password'),
        widget=forms.PasswordInput,
    )

    password_confirm = forms.CharField(
        label=_(u'New password again'),
        max_length=MAX_PASSWORD_LENGTH,
        min_length=MIN_PASSWORD_LENGTH,
        widget=forms.PasswordInput,
    )

    def __init__(self, user, *args, **kwargs):
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'content-wrapper'
        self.helper.form_method = 'post'

        self.user = user

        self.helper.layout = Layout(
            Field('password_old'),
            HTML(_(u"""<br>
                <p>Your new password:
                <ul>
                    <li>must contain at least 6 characters</li>
                    <li>must not be more than 76 characters</li>
                </ul>
                </p>
            """)),
            Field('password_new'),
            Field('password_confirm'),
            StrictButton(_('Save'), type="submit")
        )

    def save(self):
        self.user.save()