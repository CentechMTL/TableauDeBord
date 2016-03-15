# coding: utf-8

import factory
from app.home.models import UserProfile, Expertise, RoomType, Room, Rent
from django.contrib.auth.models import User, Group

from datetime import datetime

class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence('User{0}'.format)
    password = "Toto1234!#"
    is_active = True

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None) # on récupère le mot de passe ci-dessus en clair "Toto1234!#"
        my_user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            my_user.set_password(password) # on chiffre le mot de passe
            if create:
                my_user.save()
        return my_user

class UserProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)

class StaffUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence('StaffUser{0}'.format)
    password = "Toto1234!#"

    is_active = True

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(StaffUserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()

        group_staff = Group.objects.filter(name="Centech").first()
        if group_staff is None:
            group_staff = Group(name="Centech")
            group_staff.save()

        user.groups.add(group_staff)

        user.save()
        return user

class StaffUserProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(StaffUserFactory)

class ExecutiveUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence('ExecutiveUser{0}'.format)
    password = "Toto1234!#"

    is_active = True

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(ExecutiveUserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()

        group_executive = Group.objects.filter(name="Executive").first()
        if group_executive is None:
            group_executive = Group(name="Executive")
            group_executive.save()

        user.groups.add(group_executive)

        user.save()
        return user

class ExecutiveUserProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(ExecutiveUserFactory)

class ExpertiseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Expertise

    expertise = factory.Sequence('Expertise N°{0}'.format)


class RoomTypeFactory(factory.DjangoModelFactory):
    class Meta:
        model = RoomType

    name = factory.Sequence('Room type N°{0}'.format)
    is_rental = False

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
        kwargs['date_start'] = kwargs.pop('date_start', datetime.today())
        kwargs['date_end'] = kwargs.pop('date_end', datetime.today())

        rent = super(RentFactory, cls)._prepare(create, **kwargs)

        rent.save()
        return rent
