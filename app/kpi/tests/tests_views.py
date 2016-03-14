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
from app.kpi.factories import KPIFactory

from app.kpi.models import KPI_TYPE_CHOICES


class FinanceTests(TestCase):

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

        self.irl = KPIFactory(
            company=self.company,
            level=1,
            type=KPI_TYPE_CHOICES[0]
        )

        self.trl = KPIFactory(
            company=self.company,
            level=1,
            type=KPI_TYPE_CHOICES[1]
        )

    def test_trl_filter(self):
        """
        To test the trl detail of a company.
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
                'kpi:trl_filter',
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
                'kpi:trl_filter',
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
                'kpi:trl_filter',
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
                'kpi:trl_filter',
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
                'kpi:trl_filter',
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
                'kpi:trl_filter',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_irl_filter(self):
        """
        To test the irl detail of a company.
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
                'kpi:irl_filter',
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
                'kpi:irl_filter',
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
                'kpi:irl_filter',
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
                'kpi:irl_filter',
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
                'kpi:irl_filter',
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
                'kpi:irl_filter',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_trl_add(self):
        """
        To add a trl
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
                'kpi:trl_add',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Founders of the company
        """
        self.client.logout()
        self.client.login(
            username=self.founderCompany.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'kpi:trl_add',
                args=[self.company.id]
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
                'kpi:trl_add',
                args=[self.company.id]
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
                'kpi:trl_add',
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
                'kpi:trl_add',
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
                'kpi:trl_add',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_irl_add(self):
        """
        To add a irl
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
                'kpi:irl_add',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Founders of the company
        """
        self.client.logout()
        self.client.login(
            username=self.founderCompany.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'kpi:irl_add',
                args=[self.company.id]
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
                'kpi:irl_add',
                args=[self.company.id]
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
                'kpi:irl_add',
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
                'kpi:irl_add',
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
                'kpi:irl_add',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_trl_update(self):
        """
        To update a trl
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
                'kpi:trl_update',
                kwargs={
                    'pk': self.trl.id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Founders of the company
        """
        self.client.logout()
        self.client.login(
            username=self.founderCompany.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'kpi:trl_update',
                kwargs={
                    'pk': self.trl.id
                }
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
                'kpi:trl_update',
                kwargs={
                    'pk': self.trl.id
                }
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
                'kpi:trl_update',
                kwargs={
                    'pk': self.trl.id
                }
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
                'kpi:trl_update',
                kwargs={
                    'pk': self.trl.id
                }
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
                'kpi:trl_update',
                kwargs={
                    'pk': self.trl.id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_irl_update(self):
        """
        To update a irl
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
                'kpi:irl_update',
                kwargs={
                    'pk': self.irl.id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Founders of the company
        """
        self.client.logout()
        self.client.login(
            username=self.founderCompany.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'kpi:irl_update',
                kwargs={
                    'pk': self.irl.id
                }
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
                'kpi:irl_update',
                kwargs={
                    'pk': self.irl.id
                }
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
                'kpi:irl_update',
                kwargs={
                    'pk': self.irl.id
                }
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
                'kpi:irl_update',
                kwargs={
                    'pk': self.irl.id
                }
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
                'kpi:irl_update',
                kwargs={
                    'pk': self.irl.id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_trl_delete(self):
        """
        To delete a trl
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
                'kpi:trl_delete',
                kwargs={
                    'pk': self.trl.id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Founders of the company
        """
        self.client.logout()
        self.client.login(
            username=self.founderCompany.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'kpi:trl_delete',
                kwargs={
                    'pk': self.trl.id
                }
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
                'kpi:trl_delete',
                kwargs={
                    'pk': self.trl.id
                }
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
                'kpi:trl_delete',
                kwargs={
                    'pk': self.trl.id
                }
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
                'kpi:trl_delete',
                kwargs={
                    'pk': self.trl.id
                }
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
                'kpi:trl_delete',
                kwargs={
                    'pk': self.trl.id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_irl_delete(self):
        """
        To delete a irl
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
                'kpi:irl_delete',
                kwargs={
                    'pk': self.irl.id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 200)

        """
        No Access : Founders of the company
        """
        self.client.logout()
        self.client.login(
            username=self.founderCompany.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'kpi:irl_delete',
                kwargs={
                    'pk': self.irl.id
                }
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
                'kpi:irl_delete',
                kwargs={
                    'pk': self.irl.id
                }
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
                'kpi:irl_delete',
                kwargs={
                    'pk': self.irl.id
                }
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
                'kpi:irl_delete',
                kwargs={
                    'pk': self.irl.id
                }
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
                'kpi:irl_delete',
                kwargs={
                    'pk': self.irl.id
                }
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)
