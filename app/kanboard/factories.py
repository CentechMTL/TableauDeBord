# coding: utf-8

import factory

from app.kanboard.models import Card

class CardFactory(factory.DjangoModelFactory):
    class Meta:
        model = Card

    title = factory.Sequence('Card ïtrema N°{0}'.format)

    @classmethod
    def __init__(self, **kwargs):
        phase = kwargs.pop('phase', None)
        company = kwargs.pop('company', None)
        order = kwargs.pop('order', None)

        card = super(ArchiveFactory, self).__init__(self, **kwargs)

        card.save()