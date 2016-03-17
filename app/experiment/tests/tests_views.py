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
from app.experiment.factories import CustomerExperimentFactory


class ExperimentTests(TestCase):

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

        self.experiment = CustomerExperimentFactory(
            company=self.company,
            hypothesis="Hypothesis of the experiment",
            experiment_description="description of this experiment",
            test_subject_count=10,
            test_subject_description="description of subject test"
        )

    def test_experiment_list(self):
        """
        To test the experiment list of a company.
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
                'experiment:experiment_list',
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
                'experiment:experiment_list',
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
                'experiment:experiment_list',
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
                'experiment:experiment_list',
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
                'experiment:experiment_list',
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
                'experiment:experiment_list',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_experiment_add(self):
        """
        To test the experiment list of a company.
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
                'experiment:experiment_add',
                args=[self.company.id]
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
                'experiment:experiment_add',
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
                'experiment:experiment_add',
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
                'experiment:experiment_add',
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
                'experiment:experiment_add',
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
                'experiment:experiment_add',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_experiment_update(self):
        """
        To test the experiment list of a company.
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
                'experiment:experiment_update',
                args=[self.experiment.id]
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
                'experiment:experiment_update',
                args=[self.experiment.id]
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
                'experiment:experiment_update',
                args=[self.experiment.id]
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
                'experiment:experiment_update',
                args=[self.experiment.id]
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
                'experiment:experiment_update',
                args=[self.experiment.id]
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
                'experiment:experiment_update',
                args=[self.experiment.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_experiment_delete(self):
        """
        To test the experiment list of a company.
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
                'experiment:experiment_delete',
                args=[self.experiment.id]
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
                'experiment:experiment_delete',
                args=[self.experiment.id]
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
                'experiment:experiment_delete',
                args=[self.experiment.id]
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
                'experiment:experiment_delete',
                args=[self.experiment.id]
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
                'experiment:experiment_delete',
                args=[self.experiment.id]
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
                'experiment:experiment_delete',
                args=[self.experiment.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)
