# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from app.company.models import Company
from django.utils import timezone
from app.businessCanvas.models import BusinessCanvasElement

VALUE_PROPOSITION_CANVAS_TYPE_CHOICES = (
    ('Gain', 'Gain'),
    ('Pain', 'Pain'),
    ('customerJob', 'customerJob'),
    ('GainCreator', 'GainCreator'),
    ('PainReliever', 'PainReliever'),
    ('ProductAndService', 'ProductAndService'),
)

#Elements of canvas
class ValuePropositionCanvasElement(models.Model):
    class Meta:
        verbose_name = _('Value proposition canvas element')

    title = models.CharField(max_length=200)
    comment = models.TextField(blank=True,max_length=2000)
    type = models.CharField(max_length=20, choices=VALUE_PROPOSITION_CANVAS_TYPE_CHOICES, verbose_name=_('Type'))
    valueProposition = models.ForeignKey(BusinessCanvasElement, verbose_name=_('Value proposition'))

    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=_('Date of creation'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Date of updated'))

    def __str__(self):
        return self.title