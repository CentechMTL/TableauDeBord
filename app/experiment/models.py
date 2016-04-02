# coding: utf-8

from django.db import models
from app.company.models import Company
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy


# Experimentation of companies
class CustomerExperiment(models.Model):
    company = models.ForeignKey(
        Company,
        verbose_name=_('Company'),
        related_name="experiments"
    )

    # date
    dateStart = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name=_('Start date')
    )
    dateFinish = models.DateTimeField(
        auto_now=True,
        verbose_name=_('End date')
    )

    hypothesis = models.TextField(
        max_length=512,
        verbose_name=_('Hypothesis')
    )

    # null -> No define | True -> Validated | False -> Unvalidated
    validated = models.NullBooleanField(
        blank=True,
        null=True,
        verbose_name=_('Validation')
    )

    experiment_description = models.TextField(
        max_length=1024,
        verbose_name=_('Experiment description')
    )
    test_subject_count = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Number of test participants')
    )
    test_subject_description = models.TextField(
        max_length=512,
        verbose_name=_('Test description')
    )
    conclusions = models.TextField(
        max_length=512,
        blank=True,
        verbose_name=_('Conclusion')
    )

    def __unicode__(self):
        return self.hypothesis

    def get_absolute_url(self):
        return reverse_lazy(
            'experiment:experiment_list',
            args={self.company.id}
        )
