# coding: utf-8

from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

from app.founder.factories import FounderFactory
from app.mentor.factories import MentorFactory
from app.home.factories import UserFactory, StaffUserProfileFactory, \
    ExecutiveUserProfileFactory


class FounderTests(TestCase):

    def setUp(self):
        settings.EMAIL_BACKEND = \
            'django.core.mail.backends.locmem.EmailBackend'
        self.founder = FounderFactory()
        self.mentor = MentorFactory()
        self.staff = StaffUserProfileFactory()
        self.executive = ExecutiveUserProfileFactory()

    def test_index(self):
        """
        To test the listing of the founders.
        """

        """
        Access : We are connected
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        # list of founders.
        result = self.client.get(
            reverse('founder:index'),
            follow=False
        )
        self.assertEqual(result.status_code, 200)
        self.assertEqual(1, len(result.context['filter']))

        nb_founder = len(result.context['filter'])

        """
        No Access : We are not connected
        """
        self.client.logout()

        # list of founders.
        result = self.client.get(
            reverse('founder:index'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        Access : Executive
        """
        self.client.logout()
        self.client.login(
            username=self.executive.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse('founder:index'),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Context data

        Check filter, who contains all founders.
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        # create strange founder
        founderWeird = FounderFactory()
        founderWeird.user.username = u"ïtrema718"
        founderWeird.save()

        # list of founders.
        result = self.client.get(
            reverse('founder:index'),
            follow=False
        )
        self.assertEqual(result.status_code, 200)
        self.assertEqual(nb_founder+1, len(result.context['filter']))

    def test_detail(self):
        """
        To test the detail of a founder.
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
            reverse(
                'founder:detail',
                kwargs={
                    'pk': self.founder.userProfile_id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Not logged
        """
        self.client.logout()

        result = self.client.get(
            reverse(
                'founder:detail',
                kwargs={
                    'pk': self.founder.userProfile_id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        Access : Executive
        """
        self.client.logout()
        self.client.login(
            username=self.executive.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'founder:detail',
                kwargs={
                    'pk': self.founder.userProfile_id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access of an inexistant founder
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'founder:detail',
                kwargs={
                    'pk': 999999
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 404)

    def test_create(self):
        """
        To test the creation of a founder.
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
            reverse('founder:add'),
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
            reverse('founder:add'),
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
            reverse('founder:add'),
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
            reverse('founder:add'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Not logged
        """
        self.client.logout()

        result = self.client.get(
            reverse('founder:add'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_update(self):
        """
        To test update a founder.
        """

        founderTest = FounderFactory()

        """
        Access : Staff
        """
        self.client.logout()
        self.assertTrue(
            self.client.login(
                username=self.staff.user.username,
                password="Toto1234!#"
            )
        )

        result = self.client.get(
            reverse(
                'founder:update',
                kwargs={
                    'pk': founderTest.userProfile_id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access : Founder on personnal account
        """
        # A founder
        self.client.logout()
        self.client.login(
            username=self.founder.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'founder:update',
                kwargs={
                    'pk': self.founder.userProfile_id
                }
            ),
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
            reverse(
                'founder:update',
                kwargs={
                    'pk': founderTest.userProfile_id
                }
            ),
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
            reverse(
                'founder:update',
                kwargs={
                    'pk': founderTest.userProfile_id
                }
            ),
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
            reverse(
                'founder:update',
                kwargs={
                    'pk': founderTest.userProfile_id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Not logged
        """
        self.client.logout()

        result = self.client.get(
            reverse(
                'founder:update',
                kwargs={
                    'pk': founderTest.userProfile_id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        Access of an inexistant founder
        """
        self.client.logout()
        self.client.login(
            username=self.staff.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'founder:update',
                kwargs={
                    'pk': 999999
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 404)
