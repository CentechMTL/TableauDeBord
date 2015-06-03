# coding: utf-8

from django.db import models
from app.company.models import Company, CompanyStatus
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy

#Type of kpi (ex: IRL)
class KpiType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#KPIs
class KPI(models.Model):
    company = models.ForeignKey(Company)
    phase = models.ForeignKey(CompanyStatus)
    type = models.ForeignKey(KpiType)
    level = models.IntegerField(choices=((0, 0),(1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9)))
    period_start = models.DateField(auto_now_add=True, auto_now=False,)
    comment = models.TextField(blank=True, default="")

    def __str__(self):
        return self.company.name

    def get_absolute_url(self):
        if(self.type == KpiType.objects.get(name ="IRL")):
            return reverse_lazy('irl_filter', args={self.company.id})
        else:
            return reverse_lazy('trl_filter', args={self.company.id})
