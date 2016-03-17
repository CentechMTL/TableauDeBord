# coding: utf-8

import factory

from app.finance.models import Bourse, Subvention, Investissement, Pret, Vente
from app.company.factories import CompanyFactory


class BourseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Bourse

    name = factory.Sequence('Bourse ïtrema755 N°{0}'.format)

    @classmethod
    def __init__(self, **kwargs):
        dateSoumission = kwargs.pop('dateSoumission', None)
        sommeSoumission = kwargs.pop('sommeSoumission', None)
        company = kwargs.pop('company', None)

        bourse = super(BourseFactory, self).__init__(self, **kwargs)

        bourse.save()


class SubventionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Subvention

    name = factory.Sequence('Subvention ïtrema755 N°{0}'.format)

    @classmethod
    def __init__(self, **kwargs):
        dateSoumission = kwargs.pop('dateSoumission', None)
        sommeSoumission = kwargs.pop('sommeSoumission', None)
        company = kwargs.pop('company', None)

        subvention = super(SubventionFactory, self).__init__(self, **kwargs)

        subvention.save()


class InvestissementFactory(factory.DjangoModelFactory):
    class Meta:
        model = Investissement

    name = factory.Sequence('Investissement ïtrema755 N°{0}'.format)

    @classmethod
    def __init__(self, **kwargs):
        dateSoumission = kwargs.pop('dateSoumission', None)
        sommeSoumission = kwargs.pop('sommeSoumission', None)
        company = kwargs.pop('company', None)

        investissement = super(InvestissementFactory, self).\
            __init__(self, **kwargs)

        investissement.save()


class PretFactory(factory.DjangoModelFactory):
    class Meta:
        model = Pret

    name = factory.Sequence('Pret ïtrema755 N°{0}'.format)

    @classmethod
    def __init__(self, **kwargs):
        dateSoumission = kwargs.pop('dateSoumission', None)
        sommeSoumission = kwargs.pop('sommeSoumission', None)
        company = kwargs.pop('company', None)

        pret = super(PretFactory, self).__init__(self, **kwargs)

        pret.save()


class VenteFactory(factory.DjangoModelFactory):
    class Meta:
        model = Vente

    name = factory.Sequence('Vente ïtrema755 N°{0}'.format)

    @classmethod
    def __init__(self, **kwargs):
        dateSoumission = kwargs.pop('dateSoumission', None)
        sommeSoumission = kwargs.pop('sommeSoumission', None)
        company = kwargs.pop('company', None)

        vente = super(VenteFactory, self).__init__(self, **kwargs)

        vente.save()
