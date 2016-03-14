# coding: utf-8

import factory
from app.founder.models import Founder
from app.home.factories import UserFactory
from django.contrib.auth.models import User


class FounderFactory(factory.DjangoModelFactory):
    class Meta:
        model = Founder

    user = factory.SubFactory(UserFactory)
