# coding: utf-8

import factory
from app.home.models import UserProfile, Expertise
from django.contrib.auth.models import User

class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence('User N°{0}'.format)

class UserProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = UserProfile

    user = factory.SubFactory(UserFactory)

class ExpertiseFactory(factory.DjangoModelFactory):
    class Meta:
        model = Expertise

    expertise = factory.Sequence('Expertise N°{0}'.format)
