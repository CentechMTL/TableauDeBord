# coding: utf-8

import factory
from app.home.models import UserProfile, Expertise
from django.contrib.auth.models import User, Group

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

class ExpertiseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Expertise

    expertise = factory.Sequence('Expertise N°{0}'.format)

