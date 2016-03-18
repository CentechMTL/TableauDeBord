# coding: utf-8

from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase

from app.founder.factories import FounderFactory
from app.mentor.factories import MentorFactory
from app.home.factories import StaffUserProfileFactory, \
    ExecutiveUserProfileFactory
from app.company.factories import CompanyStatusFactory


class FounderTests(TestCase):

    def setUp(self):
        settings.EMAIL_BACKEND = \
            'django.core.mail.backends.locmem.EmailBackend'
        self.founder = FounderFactory()
        self.mentor = MentorFactory()
        self.staff = StaffUserProfileFactory()
        self.executive = ExecutiveUserProfileFactory()

        self.status = CompanyStatusFactory()

    def test_summary(self):
        """
        To test the display of the summary
        """

        """
        Access : Staff
        """
        # General
        self.client.logout()
        self.client.login(
            username=self.staff.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('home:summary'),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        # Specific status
        self.client.logout()
        self.client.login(
            username=self.staff.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('home:summary', kwargs={'status': self.status.id}),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access : Executive
        """
        # General
        self.client.logout()
        self.client.login(
            username=self.executive.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('home:summary'),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        # Specific status
        self.client.logout()
        self.client.login(
            username=self.executive.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('home:summary', kwargs={'status': self.status.id}),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Not staff or executive
        """
        # A founder
        self.client.logout()
        self.client.login(
            username=self.founder.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('home:summary'),
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
            reverse('home:summary'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Inexistant status
        """
        # Specific status
        self.client.logout()
        self.client.login(
            username=self.staff.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('home:summary', kwargs={'status': 999999}),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

    def test_maStartup(self):
        """
        To test the creation of a founder.
        """

        """
        Access : Staff
        """
        self.client.logout()
        self.client.login(
            username=self.staff.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('home:maStartup'),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access : Founder
        """
        self.client.logout()
        self.client.login(
            username=self.founder.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('home:maStartup'),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access : Mentor
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('home:maStartup'),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Executive
        """
        self.client.logout()
        self.client.login(
            username=self.executive.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('home:maStartup'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Not logged
        """
        self.client.logout()

        result = self.client.get(
            reverse('home:maStartup'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)
