# coding: utf-8

import factory
from app.businessCanvas.models import BusinessCanvasElement, Archive


class BusinessCanvasElementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BusinessCanvasElement

    title = factory.Sequence('BusinessCanvasElementFactory ïtrema N°{0}'.
                             format)

    @classmethod
    def __init__(self, **kwargs):
        type = kwargs.pop('type', None)
        company = kwargs.pop('company', None)

        element = super(BusinessCanvasElementFactory, self).\
            __init__(self, **kwargs)

        element.save()


class ArchiveFactory(factory.DjangoModelFactory):
    class Meta:
        model = Archive

    @classmethod
    def __init__(self, **kwargs):
        company = kwargs.pop('company', None)

        archive = super(ArchiveFactory, self).\
            __init__(self, **kwargs)

        archive.save()
