# coding: utf-8

import factory
from app.company.models import Company, CompanyStatus
from app.founder.factories import FounderFactory

class CompanyStatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CompanyStatus

    status = factory.Sequence('Status No{0}'.format)


class CompanyFactory(factory.DjangoModelFactory):
    class Meta:
        model = Company

    name = factory.Sequence('Company No{0}'.format)
    companyStatus = factory.SubFactory(CompanyStatusFactory)
