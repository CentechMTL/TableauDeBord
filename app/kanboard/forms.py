# coding: utf-8

from django.contrib.admin.widgets import AdminDateWidget
from django.forms import widgets
from django import forms

from app.kanboard.models import Card, Phase

from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, \
    Submit, Field, ButtonHolder, Hidden, Div

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['phase', 'title', 'comment', 'deadline']
        widgets = {
            'deadline' : forms.DateInput(attrs={'type':'date'})
        }

    phase = forms.ModelChoiceField(
        label = _(u"Phase"),
        queryset = Phase.objects.all(),
        required = True,
        empty_label = None
    )
    phase.widget.attrs.update({'id':'phase'})

    title = forms.CharField(
        label = _('Title'),
        required = True,
    )
    title.widget.attrs.update({'placeholder': _(u'Titre'), 'id':'title'})

    comment = forms.CharField(
        label = _('Comment'),
        required = False,
        widget = forms.Textarea(
            attrs = {
                'placeholder': _(u'Write here a brief description.'),
                'id': 'comment',
                'style': 'height: 100px; width:100%;'
            }
        )
    )

    deadline = forms.DateField()
    deadline.widget.attrs.update({'id':'deadline'})

    def __init__(self, company, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'content-wrapper'
        self.helper.form_method = 'post'

        self.fields['phase'].queryset = Phase.objects.filter(company = company)
