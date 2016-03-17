# coding: utf-8

import factory

from app.kpi.models import KPI, KPI_TYPE_CHOICES


class KPIFactory(factory.DjangoModelFactory):
    class Meta:
        model = KPI

    comment = factory.Sequence('Commentaire de Kpi ïtrema755 N°{0}'.format)

    @classmethod
    def __init__(self, **kwargs):
        level = kwargs.pop('level', None)
        type = kwargs.pop('type', None)
        company = kwargs.pop('company', None)

        kpi = super(KPIFactory, self).__init__(self, **kwargs)

        kpi.save()
