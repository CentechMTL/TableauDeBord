# coding: utf-8

from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

import time

from app.founder.factories import FounderFactory
from app.mentor.factories import MentorFactory
from app.home.factories import UserFactory, StaffUserFactory
from app.company.factories import CompanyStatusFactory, CompanyFactory
from app.kanboard.factories import PhaseFactory, CardFactory

from app.businessCanvas.models import BUSINESS_CANVAS_TYPE_CHOICES

class KanboardTests(TestCase):

    def setUp(self):
        settings.EMAIL_BACKEND = \
            'django.core.mail.backends.locmem.EmailBackend'

        self.founder = FounderFactory()
        self.mentor = MentorFactory()
        self.staff = StaffUserFactory()

        self.founderCompany = FounderFactory()
        self.mentorCompany = MentorFactory()
        self.status = CompanyStatusFactory()
        self.company = CompanyFactory(companyStatus = self.status)
        self.company.founders.add(self.founderCompany)
        self.company.mentors.add(self.mentorCompany)
        self.company.save()

        self.phase = PhaseFactory(company = self.company,
                                  order = 1)

        self.card = CardFactory(phase = self.phase,
                                order = 1)
        self.card2 = CardFactory(phase = self.phase,
                                 order = 2)

    def test_kanboard(self):
        """
        To test the kanboard of a company.
        """

        """
        Access : Staff
        """
        self.client.logout()
        self.client.login(username=self.staff.username, password="Toto1234!#")

        result = self.client.get(
            reverse('kanboard:kanboard', args= [self.company.id]),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access : Founders of the company
        """
        self.client.logout()
        self.client.login(username=self.founderCompany.user.username, password="Toto1234!#")

        result = self.client.get(
            reverse('kanboard:kanboard', args= [self.company.id]),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access : Mentors of the company
        """
        self.client.logout()
        self.client.login(username=self.mentorCompany.user.username, password="Toto1234!#")

        result = self.client.get(
            reverse('kanboard:kanboard', args= [self.company.id]),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Other founders
        """
        self.client.logout()
        self.client.login(username=self.founder.user.username, password="Toto1234!#")

        result = self.client.get(
            reverse('kanboard:kanboard', args= [self.company.id]),
            follow=False
        )
        self.assertEqual(result.status_code, 302)


        """
        No Access : Other mentors
        """
        self.client.logout()
        self.client.login(username=self.mentor.user.username, password="Toto1234!#")

        result = self.client.get(
            reverse('kanboard:kanboard', args= [self.company.id]),
            follow=False
        )
        self.assertEqual(result.status_code, 302)