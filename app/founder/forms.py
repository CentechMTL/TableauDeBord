# coding: utf-8

from django import forms
import django_filters
from app.founder.models import Founder
from app.home.models import Expertise, Education

from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, \
    Submit, Field, ButtonHolder, Hidden, Div

class FounderFilter(django_filters.FilterSet):
    class Meta:
        model = Founder
        fields = ['expertise']

class FounderUpdateForm(forms.Form):

    firstname = forms.CharField(
        label=('First name'),
        required=True,
    )
    firstname.widget.attrs.update({'placeholder': (u'First name')})

    lastname = forms.CharField(
        label="Last name",
        required=True,
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

    education = forms.ModelChoiceField(
        label=(u"Education"),
        queryset=Education.objects.all(),
        required=False,
        empty_label=None
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
            Field('firstname'),
            Field('lastname'),
            Field('phone'),
            Field('website'),
            Field('education'),
            Field('expertise'),
            HTML(u"""Utilisez la touche ctrl de votre clavier pour en sélectionner plusieurs. <br>Si il manque un domaine que vous aimeriez voir ajouter à cette liste, n'hésiter pas a en parler a l'équipe du Centech"""),
            Field('about'),
            StrictButton('Enregistrer', type="submit")
        )

    def save(self):
        self.founder.save()
        self.founder.user.save()