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
from app.finance.factories import BourseFactory, SubventionFactory, \
    InvestissementFactory, PretFactory, VenteFactory


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

        self.bourse = BourseFactory(
            company=self.company,
            dateSoumission=time.strftime("%Y-%m-%d"),
            sommeSoumission=10000
        )

        self.subvention = SubventionFactory(
            company=self.company,
            dateSoumission=time.strftime("%Y-%m-%d"),
            sommeSoumission=10000
        )

        self.investissement = InvestissementFactory(
            company=self.company,
            dateSoumission=time.strftime("%Y-%m-%d"),
            sommeSoumission=10000
        )

        self.pret = PretFactory(
            company=self.company,
            dateSoumission=time.strftime("%Y-%m-%d"),
            sommeSoumission=10000
        )

        self.vente = VenteFactory(
            company=self.company,
            dateSoumission=time.strftime("%Y-%m-%d"),
            sommeSoumission=10000
        )

    def test_detail_finance(self):
        """
        To test the finance detail of a company.
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
                'finance:detail_finance',
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
                'finance:detail_finance',
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
                'finance:detail_finance',
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
                'finance:detail_finance',
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
                'finance:detail_finance',
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
                'finance:detail_finance',
                args=[self.company.id]
            ),
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
        self.client.login(
            username=self.staff.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:bourse_add',
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
                'finance:bourse_add',
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
                'finance:bourse_add',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:bourse_add',
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
                'finance:bourse_add',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_bourse_update(self):
        """
        To test the finance detail of a company.
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
                'finance:bourse_update',
                args=[self.bourse.id]
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
                'finance:bourse_update',
                args=[self.bourse.id]
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
                'finance:bourse_update',
                args=[self.bourse.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:bourse_update',
                args=[self.bourse.id]
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
                'finance:bourse_update',
                args=[self.bourse.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_bourse_delete(self):
        """
        To test the finance detail of a company.
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
                'finance:bourse_delete',
                args=[self.bourse.id]
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
                'finance:bourse_delete',
                args=[self.bourse.id]
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
                'finance:bourse_delete',
                args=[self.bourse.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:bourse_delete',
                args=[self.bourse.id]
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
                'finance:bourse_delete',
                args=[self.bourse.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_subvention_add(self):
        """
        To test the finance detail of a company.
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
                'finance:subvention_add',
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
                'finance:subvention_add',
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
                'finance:subvention_add',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:subvention_add',
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
                'finance:subvention_add',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_subvention_update(self):
        """
        To test the finance detail of a company.
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
                'finance:subvention_update',
                args=[self.subvention.id]
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
                'finance:subvention_update',
                args=[self.subvention.id]
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
                'finance:subvention_update',
                args=[self.subvention.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:subvention_update',
                args=[self.subvention.id]
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
                'finance:subvention_update',
                args=[self.subvention.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_subvention_delete(self):
        """
        To test the finance detail of a company.
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
                'finance:subvention_delete',
                args=[self.subvention.id]
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
                'finance:subvention_delete',
                args=[self.subvention.id]
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
                'finance:subvention_delete',
                args=[self.subvention.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:subvention_delete',
                args=[self.subvention.id]
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
                'finance:subvention_delete',
                args=[self.subvention.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_investissement_add(self):
        """
        To test the finance detail of a company.
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
                'finance:investissement_add',
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
                'finance:investissement_add',
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
                'finance:investissement_add',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:investissement_add',
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
                'finance:investissement_add',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_investissement_update(self):
        """
        To test the finance detail of a company.
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
                'finance:investissement_update',
                args=[self.investissement.id]
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
                'finance:investissement_update',
                args=[self.investissement.id]
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
                'finance:investissement_update',
                args=[self.investissement.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:investissement_update',
                args=[self.investissement.id]
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
                'finance:investissement_update',
                args=[self.investissement.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_investissement_delete(self):
        """
        To test the finance detail of a company.
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
                'finance:investissement_delete',
                args=[self.investissement.id]
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
                'finance:investissement_delete',
                args=[self.investissement.id]
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
                'finance:investissement_delete',
                args=[self.investissement.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:investissement_delete',
                args=[self.investissement.id]
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
                'finance:investissement_delete',
                args=[self.investissement.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_pret_add(self):
        """
        To test the finance detail of a company.
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
                'finance:pret_add',
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
                'finance:pret_add',
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
                'finance:pret_add',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:pret_add',
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
                'finance:pret_add',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_pret_update(self):
        """
        To test the finance detail of a company.
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
                'finance:pret_update',
                args=[self.pret.id]
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
                'finance:pret_update',
                args=[self.pret.id]
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
                'finance:pret_update',
                args=[self.pret.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:pret_update',
                args=[self.pret.id]
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
                'finance:pret_update',
                args=[self.pret.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_pret_delete(self):
        """
        To test the finance detail of a company.
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
                'finance:pret_delete',
                args=[self.pret.id]
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
                'finance:pret_delete',
                args=[self.pret.id]
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
                'finance:pret_delete',
                args=[self.pret.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:pret_delete',
                args=[self.pret.id]
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
                'finance:pret_delete',
                args=[self.pret.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_vente_add(self):
        """
        To test the finance detail of a company.
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
                'finance:vente_add',
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
                'finance:vente_add',
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
                'finance:vente_add',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:vente_add',
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
                'finance:vente_add',
                args=[self.company.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_vente_update(self):
        """
        To test the finance detail of a company.
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
                'finance:vente_update',
                args=[self.vente.id]
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
                'finance:vente_update',
                args=[self.vente.id]
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
                'finance:vente_update',
                args=[self.vente.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:vente_update',
                args=[self.vente.id]
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
                'finance:vente_update',
                args=[self.vente.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

    def test_vente_delete(self):
        """
        To test the finance detail of a company.
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
                'finance:vente_delete',
                args=[self.vente.id]
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
                'finance:vente_delete',
                args=[self.vente.id]
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
                'finance:vente_delete',
                args=[self.vente.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)

        """
        No Access : Mentors
        """
        self.client.logout()
        self.client.login(
            username=self.mentor.user.username,
            password="Toto1234!#"
        )

        result = self.client.get(
            reverse(
                'finance:vente_delete',
                args=[self.vente.id]
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
                'finance:vente_delete',
                args=[self.vente.id]
            ),
            follow=False
        )
        self.assertEqual(result.status_code, 302)
