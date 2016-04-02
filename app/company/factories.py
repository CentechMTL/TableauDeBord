# coding: utf-8

import factory
from app.company.models import Company, CompanyStatus


class CompanyStatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CompanyStatus

    status = factory.Sequence('Status No{0}'.format)


class CompanyFactory(factory.DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Sequence('Company ïtrema755 N°{0}'.format)

    @classmethod
    def __init__(self, **kwargs):
        companyStatus = kwargs.pop('companyStatus', None)
        company = super(CompanyFactory, self).__init__(self, **kwargs)

        company.save()
