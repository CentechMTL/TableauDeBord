# coding: utf-8

from django.db import models
from app.company.models import Company, CompanyStatus
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy

KPI_TYPE_CHOICES = (
    ('IRL', 1),
    ('TRL', 2),
)


# KPIs
class KPI(models.Model):
    class Meta:
        verbose_name_plural = _('KPIs')

    company = models.ForeignKey(
        Company,
        verbose_name=_('Companies'),
        related_name="KPIs"
    )

    type = models.CharField(
        max_length=50,
        choices=KPI_TYPE_CHOICES,
        verbose_name=_('Type')
    )

    level = models.IntegerField(
        choices=(
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9)
        ),
        verbose_name=_('Level')
    )

    period_start = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name=_('Date')
    )

    comment = models.TextField(
        blank=True,
        default="",
        verbose_name=_('Comment')
    )

    def __unicode__(self):
        return self.company.name

    def get_absolute_url(self):
        if self.type == KPI_TYPE_CHOICES[0][0]:
            return reverse_lazy('kpi:irl_filter', args={self.company.id})
        else:
            return reverse_lazy('kpi:trl_filter', args={self.company.id})
