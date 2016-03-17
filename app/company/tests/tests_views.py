# coding: utf-8

from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

from app.founder.factories import FounderFactory
from app.mentor.factories import MentorFactory
from app.home.factories import UserFactory, StaffUserProfileFactory, \
    ExecutiveUserProfileFactory
from app.company.factories import CompanyFactory, CompanyStatusFactory


class CompanyTests(TestCase):

    def setUp(self):
        settings.EMAIL_BACKEND = \
            'django.core.mail.backends.locmem.EmailBackend'
        self.founder = FounderFactory()
        self.mentor = MentorFactory()
        self.staff = StaffUserProfileFactory()
        self.executive = ExecutiveUserProfileFactory()

        self.status = CompanyStatusFactory()
        self.company = CompanyFactory(companyStatus=self.status)

    def test_index(self):
        """
        To test the listing of the companies.
        """

        """
        Access

        We are connected
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        # list of companies.
        result = self.client.get(
            reverse('company:index'),
            follow=False
        )
        self.assertEqual(result.status_code, 200)
        self.assertEqual(1, len(result.context['filter']))

        nb_company = len(result.context['filter'])

        """
        No Access

        We are not connected
        """
        self.client.logout()

        # list of companies.
        result = self.client.get(
            reverse('company:index'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        Context data

        Check filter, who contains all companies
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        # create strange company
        companyWeird = CompanyFactory(companyStatus=self.status)
        companyWeird.name = u"Company ïtrema718"
        companyWeird.save()

        # list of companies.
        result = self.client.get(
            reverse('company:index'),
            follow=False
        )
        self.assertEqual(result.status_code, 200)
        self.assertEqual(nb_company+1, len(result.context['filter']))

    def test_detail(self):
        """
        To test the detail of a company.
        """

        """
        Access
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('company:detail', kwargs={'pk': self.company.id}),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Not logged
        """
        self.client.logout()

        result = self.client.get(
            reverse('company:detail', kwargs={'pk': self.company.id}),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        Access of an inexistant company
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('company:detail', kwargs={'pk': 999999}),
            follow=False
        )
        self.assertEqual(result.status_code, 404)

    def test_create(self):
        """
        To test the creation of a company.
        """

        """
        Access : Staff only
        """
        self.client.logout()
        self.assertTrue(
            self.client.login(
                username=self.staff.user.username,
                password="Toto1234!#"
            )
        )

        result = self.client.get(
            reverse('company:create'),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Not in the staff
        """
        # A founder
        self.client.logout()
        self.client.login(
            username=self.founder.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('company:create'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        # A mentor
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('company:create'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        # An executive
        self.client.logout()
        self.client.login(
            username=self.executive.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('company:create'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Not logged
        """
        self.client.logout()

        result = self.client.get(
            reverse('company:create'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_update(self):
        """
        To test update a company.
        """

        """
        Access : Staff only
        """
        self.client.logout()
        self.assertTrue(
            self.client.login(
                username=self.staff.user.username,
                password="Toto1234!#"
            )
        )

        result = self.client.get(
            reverse('company:update', kwargs={'pk': self.company.id}),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access : Founder on personnal company
        """
        companyTest = CompanyFactory(companyStatus=self.status)
        founderTest = FounderFactory()
        companyTest.founders.add(founderTest)
        companyTest.save()

        self.client.logout()
        self.client.login(
            username=founderTest.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('company:update', kwargs={'pk': companyTest.id}),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Not in the staff
        """
        # A founder
        self.client.logout()
        self.client.login(
            username=self.founder.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('company:update', kwargs={'pk': self.company.id}),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        # A mentor
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('company:update', kwargs={'pk': self.company.id}),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        # An executive
        self.client.logout()
        self.client.login(
            username=self.executive.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('company:update', kwargs={'pk': self.company.id}),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Not logged
        """
        self.client.logout()

        result = self.client.get(
            reverse('company:update', kwargs={'pk': self.company.id}),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        Access of an inexistant company
        """
        self.client.logout()
        self.client.login(
            username=self.staff.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('company:update', kwargs={'pk': 999999}),
            follow=False
        )
        self.assertEqual(result.status_code, 404)

    def test_create_status(self):
        """
        To test create a status.
        """

        """
        Access : Staff only
        """
        self.client.logout()
        self.assertTrue(
            self.client.login(
                username=self.staff.user.username,
                password="Toto1234!#"
            )
        )

        result = self.client.get(
            reverse('company:status_create'),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Not in the staff
        """
        # A founder
        self.client.logout()
        self.client.login(
            username=self.founder.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('company:status_create'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        # A mentor
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('company:status_create'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        # An executive
        self.client.logout()
        self.client.login(
            username=self.executive.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('company:status_create'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Not logged
        """
        self.client.logout()

        result = self.client.get(
            reverse('company:status_create'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)
