from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from app.company.models import Company
from django.utils import timezone

#Type (ex:pains, gains)
class ValuePropositionCanvasType(models.Model):
    class Meta:
        verbose_name = _('Value proposition canvas type')

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#Elements of canvas
class ValuePropositionCanvasElement(models.Model):
    class Meta:
        verbose_name = _('Value proposition canvas element')

    title = models.CharField(max_length=200)
    comment = models.TextField(blank=True,max_length=2000)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,)
    type = models.ForeignKey(ValuePropositionCanvasType,verbose_name=_('Type'))
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.title