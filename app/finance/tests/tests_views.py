# coding: utf-8

from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

from app.founder.factories import FounderFactory
from app.mentor.factories import MentorFactory
from app.home.factories import UserFactory, StaffUserFactory
from app.company.factories import CompanyStatusFactory, CompanyFactory

class FinanceTests(TestCase):

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


    def test_detail_finance(self):
        """
        To test the finance detail of a company.
        """

        """
        Access : Staff
        """
        self.client.logout()
        self.client.login(username=self.staff.username, password="Toto1234!#")

        result = self.client.get(
            reverse('finance:detail_finance', args= [self.company.id]),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access : Founders of the company
        """
        self.client.logout()
        self.client.login(username=self.founderCompany.user.username, password="Toto1234!#")

        result = self.client.get(
            reverse('finance:detail_finance', args= [self.company.id]),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access : Mentors of the company
        """
        self.client.logout()
        self.client.login(username=self.mentorCompany.user.username, password="Toto1234!#")

        result = self.client.get(
            reverse('finance:detail_finance', args= [self.company.id]),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Other founders
        """
        self.client.logout()
        self.client.login(username=self.founder.user.username, password="Toto1234!#")

        result = self.client.get(
            reverse('finance:detail_finance', args= [self.company.id]),
            follow=False
        )
        self.assertEqual(result.status_code, 302)


        """
        No Access : Other mentors
        """
        self.client.logout()
        self.client.login(username=self.mentor.user.username, password="Toto1234!#")

        result = self.client.get(
            reverse('finance:detail_finance', args= [self.company.id]),
            follow=False
        )
        self.assertEqual(result.status_code, 302)


    def test_bourse_add(self):
        """
        To test the finance detail of a company.
        """

        """
        Access : Staff
        """
        self.client.logout()
        self.client.login(username=self.staff.username, password="Toto1234!#")

        result = self.client.get(
            reverse('finance:bourse_add', args= [self.company.id]),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access : Founders of the company
        """
        self.client.logout()
        self.client.login(username=self.founderCompany.user.username, password="Toto1234!#")

        result = self.client.get(
            reverse('finance:bourse_add', args= [self.company.id]),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Other founders
        """
        self.client.logout()
        self.client.login(username=self.founder.user.username, password="Toto1234!#")

        result = self.client.get(
            reverse('finance:bourse_add', args= [self.company.id]),
            follow=False
        )
        self.assertEqual(result.status_code, 302)


        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(username=self.mentor.user.username, password="Toto1234!#")

        result = self.client.get(
            reverse('finance:bourse_add', args= [self.company.id]),
            follow=False
        )
        self.assertEqual(result.status_code, 302)