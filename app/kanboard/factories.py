# coding: utf-8

import factory

from app.kanboard.models import Card, Phase

class PhaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Phase

    title = factory.Sequence('Phase ïtrema N°{0}'.format)

    @classmethod
    def __init__(self, **kwargs):
        company = kwargs.pop('company', None)
        order = kwargs.pop('order', None)

        phase = super(BusinessCanvasElementFactory, self).__init__(self, **kwargs)

        phase.save()


class CardFactory(factory.DjangoModelFactory):
    class Meta:
        model = Card

    title = factory.Sequence('Card ïtrema N°{0}'.format)

    @classmethod
    def __init__(self, **kwargs):
        phase = kwargs.pop('phase', None)
        order = kwargs.pop('order', None)

        card = super(ArchiveFactory, self).__init__(self, **kwargs)

        card.save()