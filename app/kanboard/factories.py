# coding: utf-8

import factory
from app.kanboard.models import Card, Comment, PHASE_CHOICES


class CardFactory(factory.DjangoModelFactory):
    class Meta:
        model = Card

    title = factory.Sequence('Card ïtrema755 N°{0}'.format)

    @classmethod
    def __init__(self, **kwargs):
        company = kwargs.pop('company', None)
        phase = kwargs.pop('phase', None)
        state = kwargs.pop('state', None)

        card = super(CardFactory, self).__init__(self, **kwargs)

        card.save()


class CommentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Card

    comment = factory.Sequence('Comment ïtrema755 N°{0}'.format)

    @classmethod
    def __init__(self, **kwargs):
        card = kwargs.pop('card', None)
        creator = kwargs.pop('creator', None)

        comment = super(CommentFactory, self).__init__(self, **kwargs)

        comment.save()
