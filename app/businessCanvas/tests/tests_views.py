# coding: utf-8

from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase
import time
from app.founder.factories import FounderFactory
from app.mentor.factories import MentorFactory
from app.home.factories import UserFactory, StaffUserProfileFactory, \
    ExecutiveUserProfileFactory
from app.company.factories import CompanyStatusFactory, CompanyFactory
from app.businessCanvas.factories import BusinessCanvasElementFactory, \
    ArchiveFactory
from app.businessCanvas.models import BUSINESS_CANVAS_TYPE_CHOICES


class BusinessCanvasTests(TestCase):

    def setUp(self):
        settings.EMAIL_BACKEND = \
            'django.core.mail.backends.locmem.EmailBackend'

        self.founder = FounderFactory()
        self.mentor = MentorFactory()
        self.staff = StaffUserProfileFactory()
        self.executive = ExecutiveUserProfileFactory()

        self.founderCompany = FounderFactory()
        self.mentorCompany = MentorFactory()
        self.status = CompanyStatusFactory()
        self.company = CompanyFactory(companyStatus=self.status)
        self.company.founders.add(self.founderCompany)
        self.company.mentors.add(self.mentorCompany)
        self.company.save()

        self.element = BusinessCanvasElementFactory(
            company=self.company,
            type=BUSINESS_CANVAS_TYPE_CHOICES[0][0]
        )

        self.element2 = BusinessCanvasElementFactory(
            company=self.company,
            type=BUSINESS_CANVAS_TYPE_CHOICES[1][0]
        )

        self.archive = ArchiveFactory(company=self.company)
        self.archive.elements.add(self.element)

    def test_businessCanvasElement_list(self):
        """
        To test the business canvas list of a company.
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
            reverse(
                'businessCanvas:businessCanvasElement_list',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access : Founders of the company
        """
        self.client.logout()
        self.client.login(
            username=self.founderCompany.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasElement_list',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access : Mentors of the company
        """
        self.client.logout()
        self.client.login(
            username=self.mentorCompany.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasElement_list',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Other founders
        """
        self.client.logout()
        self.client.login(
            username=self.founder.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasElement_list',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Other mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasElement_list',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Executive
        """
        self.client.logout()
        self.client.login(
            username=self.executive.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasElement_list',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_businessCanvasElementArchived_list(self):
        """
        To test the business canvas archived list of a company.
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
            reverse(
                'businessCanvas:businessCanvasElementArchived_list',
                args=[self.archive.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access : Founders of the company
        """
        self.client.logout()
        self.client.login(
            username=self.founderCompany.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasElementArchived_list',
                args=[self.archive.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        Access : Mentors of the company
        """
        self.client.logout()
        self.client.login(
            username=self.mentorCompany.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasElementArchived_list',
                args=[self.archive.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Other founders
        """
        self.client.logout()
        self.client.login(
            username=self.founder.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasElementArchived_list',
                args=[self.archive.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Other mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasElementArchived_list',
                args=[self.archive.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Executive
        """
        self.client.logout()
        self.client.login(
            username=self.executive.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasElementArchived_list',
                args=[self.archive.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_businessCanvasDeleteArchive(self):
        """
        To test delete a business canvas archive of a company.
        """

        """
        Access : Founders of the company
        """
        self.client.logout()
        self.client.login(
            username=self.founderCompany.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasDeleteArchive',
                args=[self.archive.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Staff
        """
        self.client.logout()
        self.client.login(
            username=self.staff.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasDeleteArchive',
                kwargs={'pk': self.archive.id}
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors of the company
        """
        self.client.logout()
        self.client.login(
            username=self.mentorCompany.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasDeleteArchive',
                args=[self.archive.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Other founders
        """
        self.client.logout()
        self.client.login(
            username=self.founder.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasDeleteArchive',
                args=[self.archive.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Other mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasDeleteArchive',
                args=[self.archive.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Executive
        """
        self.client.logout()
        self.client.login(
            username=self.executive.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'businessCanvas:businessCanvasDeleteArchive',
                args=[self.archive.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)
