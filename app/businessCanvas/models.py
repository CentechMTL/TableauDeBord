# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from app.company.models import Company
from django.utils import timezone

#TODO delete foreign key
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

#The type of element in the business canvas
class BusinessCanvasType(models.Model):
    class Meta:
        verbose_name = _('Business canvas type')

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#Element of the business canvas
#Can be disactivated if it's archived
class BusinessCanvasElement(models.Model):
    class Meta:
        verbose_name = _('Business canvas element')

    title = models.CharField(max_length=200)
    comment = models.TextField(blank=True,max_length=2000)
    #Created on
    date = models.DateTimeField(auto_now_add=True, auto_now=False,)
    type = models.CharField(max_length=20, choices=BUSINESS_CANVAS_TYPE_CHOICES, null=True)
    company = models.ForeignKey(Company)
    #True -> Archived | False -> Current use
    disactivated = models.BooleanField(default=False, verbose_name=_('Disactivated'))

    def __str__(self):
        return self.title

#Archive of the business canvas
#use copy of current BusinessCanvasElement
class Archive(models.Model):
    class Meta:
        verbose_name = _('Archive')

    #Created on
    date = models.DateField(auto_now_add=True, auto_now=False)
    company = models.ForeignKey(Company)
    #List of elements in the archive
    elements = models.ManyToManyField(BusinessCanvasElement,blank=True)

    def __str__(self):
        return str(self.date)
