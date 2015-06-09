# coding: utf-8

from django import forms
import django_filters
from app.mentor.models import Mentor
from app.home.models import Expertise, Education

from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, \
    Submit, Field, ButtonHolder, Hidden, Div


class MentorFilter(django_filters.FilterSet):
    class Meta:
        model = Mentor
        fields = ['expertise']

class MentorCreateForm(forms.Form):

    firstname = forms.CharField(
        label=('First name'),
        required=False,
    )
    firstname.widget.attrs.update({'placeholder': (u'First name')})

    lastname = forms.CharField(
        label="Last name",
        required=False,
    )
    lastname.widget.attrs.update({'placeholder': (u'Last name')})

    username = forms.CharField(
        label="Username",
        required=True,
    )
    username.widget.attrs.update({'placeholder': (u'Username')})

    email = forms.CharField(
        label="Email",
        required=True,
    )
    email.widget.attrs.update({'placeholder': (u'Email')})

    phone = forms.CharField(
        label=('Phone number'),
        required=False,
        max_length=10
    )
    phone.widget.attrs.update({'placeholder': (u'Phone number')})

    website = forms.URLField(
        label=('Web site'),
        required=False,
    )
    website.widget.attrs.update({'placeholder': (u'https://example.com')})

    about = forms.CharField(
        label=('Description'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': (u'Rentrez ici un bref résumé de vos compétences et de votre parcours.'),
                'class': 'md-editor'
            }
        )
    )

    expertise = forms.ModelMultipleChoiceField(
        label=(u"Aire d'expertise"),
        queryset=Expertise.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                'required': 'required',
            }
        )
    )

    picture = forms.ImageField(
        label=('Photo'),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(MentorCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'content-wrapper'
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Field('firstname'),
            Field('lastname'),
            Field('username'),
            Field('email'),
            Field('picture'),
            Field('phone'),
            Field('website'),
            Field('expertise'),
            HTML(u"""Vos domaines d'expertise.<br>
            Si il manque un domaine que vous aimeriez voir ajouter à cette liste, n'hésiter pas a en parler à l'équipe du Centech"""),
            Field('about'),
            StrictButton('Enregistrer', type="submit")
        )

class MentorUpdateForm(forms.Form):

    firstname = forms.CharField(
        label=('First name'),
        required=False,
    )
    firstname.widget.attrs.update({'placeholder': (u'First name')})

    lastname = forms.CharField(
        label="Last name",
        required=False,
    )
    lastname.widget.attrs.update({'placeholder': (u'Last name')})

    phone = forms.CharField(
        label=('Phone number'),
        required=False,
        max_length=10
    )
    phone.widget.attrs.update({'placeholder': (u'Phone number')})

    website = forms.URLField(
        label=('Web site'),
        required=False,
    )
    website.widget.attrs.update({'placeholder': (u'https://example.com')})

    about = forms.CharField(
        label=('Description'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': (u'Rentrez ici un bref résumé de vos compétences et de votre parcours.'),
                'class': 'md-editor'
            }
        )
    )

    expertise = forms.ModelMultipleChoiceField(
        label=(u"Aire d'expertise"),
        queryset=Expertise.objects.all(),
        required=False,
        widget=forms.SelectMultiple(
            attrs={
                'required': 'required',
            }
        )
    )

    picture = forms.ImageField(
        label=('Photo'),
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
            Field('firstname'),
            Field('lastname'),
            Field('picture'),
            Field('phone'),
            Field('website'),
            Field('expertise'),
            HTML(u"""Vos domaines d'expertise.<br>
            Si il manque un domaine que vous aimeriez voir ajouter à cette liste, n'hésiter pas a en parler à l'équipe du Centech"""),
            Field('about'),
            StrictButton('Enregistrer', type="submit")
        )

    def save(self):
        self.mentor.save()
        self.mentor.user.save()