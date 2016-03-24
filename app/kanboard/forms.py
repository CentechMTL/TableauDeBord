# coding: utf-8
from django import forms

from app.kanboard.models import Card, PHASE_CHOICES
from app.founder.models import Founder

from django.utils.translation import ugettext_lazy as _


class CardForm(forms.ModelForm):
    class Meta:
        model = Card

        fields = [
            'phase',
            'title',
            'comment',
            'deadline',
            'state'
        ]

        widgets = {
            'deadline': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )
        }

    state = forms.BooleanField(
        label=_('Complete'),
        widget=forms.CheckboxInput(
            attrs={
                'required': False,
                'id': 'state'
            }
        )
    )

    phase = forms.ChoiceField(
        choices=PHASE_CHOICES,
    )
    phase.widget.attrs.update({'id': 'phase'})

    title = forms.CharField(
        label=_('Title*'),
        required=True,
    )
    title.widget.attrs.update({'placeholder': _(u'Title'), 'id': 'title'})

    comment = forms.CharField(
        label=_('Comment'),
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': _(u'Write here a brief description.'),
                'id': 'comment',
                'style': 'height: 100px; width:100%;'
            }
        )
    )

    deadline = forms.DateField(
        label=_(u"Due date")
    )
    deadline.widget.attrs.update({'id': 'deadline'})

    assigned = forms.ModelChoiceField(
        label=_(u"Assign to"),
        queryset=Founder.objects.all(),
        required=True,
        empty_label="None"
    )
    assigned.widget.attrs.update({'id': 'assigned'})

    def __init__(self, company, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.fields['assigned'].queryset = Founder.objects.\
            filter(company=company)
