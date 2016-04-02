# coding: utf-8

from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

from app.founder.factories import FounderFactory
from app.mentor.factories import MentorFactory
from app.home.factories import UserFactory, StaffUserProfileFactory, \
    ExecutiveUserProfileFactory


class MentorTests(TestCase):

    def setUp(self):
        settings.EMAIL_BACKEND = \
            'django.core.mail.backends.locmem.EmailBackend'
        self.founder = FounderFactory()
        self.mentor = MentorFactory()
        self.staff = StaffUserProfileFactory()
        self.executive = ExecutiveUserProfileFactory()

    def test_index(self):
        """
        To test the listing of the mentors.
        """

        """
        Access : We are connected
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        # list of mentors.
        result = self.client.get(
            reverse('mentor:index'),
            follow=False
        )
        self.assertEqual(result.status_code, 200)
        self.assertEqual(1, len(result.context['mentorFilter']))

        nb_mentor = len(result.context['mentorFilter'])

        """
        No Access : We are not connected
        """
        self.client.logout()

        # list of mentors.
        result = self.client.get(
            reverse('mentor:index'),
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

        # list of mentors.
        result = self.client.get(
            reverse('mentor:index'),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Context data

        Check filter, who contains all mentors.
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        # create strange mentor
        mentorWeird = MentorFactory()
        mentorWeird.user.username = u"ïtrema718"
        mentorWeird.save()

        # list of mentors.
        result = self.client.get(
            reverse('mentor:index'),
            follow=False
        )
        self.assertEqual(result.status_code, 200)
        self.assertEqual(nb_mentor+1, len(result.context['mentorFilter']))

    def test_detail(self):
        """
        To test the detail of a mentor.
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
                'mentor:detail',
                kwargs={
                    'pk': self.mentor.userProfile_id
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
                'mentor:detail',
                kwargs={
                    'pk': self.mentor.userProfile_id
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
                'mentor:detail',
                kwargs={
                    'pk': self.mentor.userProfile_id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access of an inexistant mentor
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'mentor:detail',
                kwargs={
                    'pk': 999999
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 404)

    def test_create(self):
        """
        To test the creation of a mentor.
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
            reverse('mentor:create'),
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
            reverse('mentor:create'),
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
            reverse('mentor:create'),
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
            reverse('mentor:create'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Not logged
        """
        self.client.logout()

        result = self.client.get(
            reverse('mentor:create'),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_update(self):
        """
        To test update a mentor.
        """

        mentorTest = MentorFactory()

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
                'mentor:update',
                kwargs={
                    'pk': mentorTest.userProfile_id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access : Mentor on personnal account
        """
        # A mentor
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'mentor:update',
                kwargs={
                    'pk': self.mentor.userProfile_id
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
                'mentor:update',
                kwargs={
                    'pk': mentorTest.userProfile_id
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
                'mentor:update',
                kwargs={
                    'pk': mentorTest.userProfile_id
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
                'mentor:update',
                kwargs={
                    'pk': mentorTest.userProfile_id
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
                'mentor:update',
                kwargs={
                    'pk': mentorTest.userProfile_id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        Access of an inexistant mentor
        """
        self.client.logout()
        self.client.login(
            username=self.staff.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'mentor:update',
                kwargs={
                    'pk': 999999
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 404)
