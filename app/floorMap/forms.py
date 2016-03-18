# coding: utf-8

from django import forms
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from app.company.models import Company
from app.floorMap.models import Rent, Room


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['company', 'room', 'date_start', 'date_end']

    company = forms.ModelChoiceField(
        label=_(u"Company"),
        queryset=Company.objects.all().order_by('name'),
        required=True,
        initial=0,
    )

    room = forms.ModelChoiceField(
        label=_(u"Room code"),
        queryset=Room.objects.filter(type__is_rental=True).order_by('code'),
        required=True,
    )

    date_start = forms.DateField(
        label=_('Start date'),
        required=True,
        input_formats=('%Y-%m-%d',),
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'datepicker'
            }
        )
    )

    date_end = forms.DateField(
        label=_('End date'),
        required=True,
        input_formats=('%Y-%m-%d',),
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'class': 'datepicker'
            }
        )
    )

    def clean_date_end(self):
        date_start = self.cleaned_data['date_start']
        date_end = self.cleaned_data['date_end']

        if date_start > date_end:
            raise forms.ValidationError(
                _("End date cannot be before the start date!"),
                code='invalid'
            )

        return date_end

    def clean(self):
        # Always check that key exists in cleaned_data
        # before using it in clean() method.
        if ('room' and 'date_start' and 'date_end') not in self.cleaned_data:
            return self.cleaned_data

        lst_conflicting = []

        for rent in self.conflicts():
            lst_conflicting.append(rent.company.name)

        if lst_conflicting:
            str_conflicts = lst_conflicting[0]

            for name in lst_conflicting[1:-1]:
                str_conflicts = ", ".join([str_conflicts, name])

            if len(lst_conflicting) > 1:
                str_conflicts = " ".join([
                    str_conflicts,
                    str(_("and")),
                    lst_conflicting[-1:][0]
                ])

            raise forms.ValidationError({
                'room': [forms.ValidationError(
                    _("Room and date conflicts with existing rental(s) "
                      "by: %(conflicting)s."),
                    code='invalid',
                    params={'conflicting': str_conflicts}
                )]
            })

        return self.cleaned_data

    def conflicts(self):
        conflicting_period = [
            self.cleaned_data['date_start'],
            self.cleaned_data['date_end']
        ]

        results = Rent.objects.filter(
            room_id__exact=self.cleaned_data['room'].id
        ).filter(
            Q(
                date_start__range=conflicting_period
            ) | Q(
                date_end__range=conflicting_period
            )
        )

        return results


class RentalFormUpdate(RentalForm):
    class Meta:
        model = Rent
        fields = ['id', 'company', 'room', 'date_start', 'date_end']

    id = forms.CharField(
        widget=forms.HiddenInput,
    )

    def conflicts(self):
        conflicting_period = [
            self.cleaned_data['date_start'],
            self.cleaned_data['date_end']
        ]

        results = Rent.objects.filter(
            room_id__exact=self.cleaned_data['room'].id
        ).filter(
            Q(
                date_start__range=conflicting_period
            ) | Q(
                date_end__range=conflicting_period
            )
        ).exclude(
            id=int(self.cleaned_data['id'])
        )

        return results
