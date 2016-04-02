# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from app.company.models import Company
from django.utils import timezone

BUSINESS_CANVAS_TYPE_CHOICES = (
    ('KeyPartner', 1),
    ('KeyActivitie', 2),
    ('ValueProposition', 3),
    ('CustomerRelationship', 4),
    ('KeyResource', 5),
    ('Channel', 6),
    ('CustomerSegment', 7),
    ('CostStructure', 8),
    ('RevenueStream', 9),
    ('BrainstormingSpace', 10),
)


# Element of the business canvas
# Can be deactivated if it's archived
class BusinessCanvasElement(models.Model):
    class Meta:
        verbose_name = _('Business canvas element')

    title = models.CharField(
        max_length=200,
        verbose_name=_('Title')
    )
    comment = models.TextField(
        blank=True,
        max_length=2000,
        verbose_name=_('Comment')
    )
    # Created on
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name=_('Creation date')
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Update date')
    )
    type = models.CharField(
        max_length=20,
        choices=BUSINESS_CANVAS_TYPE_CHOICES,
        null=True,
        verbose_name=_('Type')
    )
    company = models.ForeignKey(
        Company,
        verbose_name=_('Company')
    )

    # True -> Archived | False -> Current use
    disactivated = models.BooleanField(
        default=False,
        verbose_name=_('Deactivated')
    )

    def __unicode__(self):
        return self.title


# Archive of the business canvas
# use copy of current BusinessCanvasElement
class Archive(models.Model):
    class Meta:
        verbose_name = _('Archive')

    # Created on
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name=_('Date')
    )
    company = models.ForeignKey(
        Company,
        verbose_name=_('Company')
    )
    # List of elements in the archive
    elements = models.ManyToManyField(
        BusinessCanvasElement,
        blank=True,
        verbose_name=_('Archive elements')
    )

    def __unicode__(self):
        return str(self.date)
