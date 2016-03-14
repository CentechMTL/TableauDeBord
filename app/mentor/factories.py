# coding: utf-8

import factory
from app.mentor.models import Mentor
from app.home.factories import UserFactory
from django.contrib.auth.models import User


class MentorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Mentor

    user = factory.SubFactory(UserFactory)
