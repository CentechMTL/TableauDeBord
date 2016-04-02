# coding: utf-8

import datetime
import factory

from app.floorMap.models import RoomType, Room, Rent


class RoomTypeFactory(factory.DjangoModelFactory):
    class Meta:
        model = RoomType

    name = factory.Sequence('Room type N°{0}'.format)
    is_rental = False
    bg_color = '#FFFFFF'
    alt_bg_color = '#CCCCCC'

    @classmethod
    def _prepare(cls, create, **kwargs):
        room_type = super(RoomTypeFactory, cls)._prepare(create, **kwargs)

        room_type.save()
        return room_type


class RoomFactory(factory.DjangoModelFactory):
    class Meta:
        model = Room

    code = factory.Sequence('C-{0}'.format)
    coords = '0,0,100,100'

    @classmethod
    def _prepare(cls, create, **kwargs):
        room = super(RoomFactory, cls)._prepare(create, **kwargs)

        room.save()
        return room


class RentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Rent

    @classmethod
    def _prepare(cls, create, **kwargs):
        kwargs['date_start'] = kwargs.pop(
            'date_start',
            datetime.datetime.today()
        )
        kwargs['date_end'] = kwargs.pop(
            'date_end',
            datetime.datetime.today()
        )

        rent = super(RentFactory, cls)._prepare(create, **kwargs)

        rent.save()
        return rent
