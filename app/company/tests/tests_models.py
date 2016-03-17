from django.test import TestCase

from app.company.factories import CompanyStatusFactory, CompanyFactory
from app.home.factories import UserFactory
from app.founder.factories import FounderFactory


class CompanyModelsTest(TestCase):

    def setUp(self):
        self.status1 = CompanyStatusFactory()
        self.company1 = CompanyFactory(companyStatus=self.status1)

    def test_get_users(self):
        self.assertEqual(0, len(self.company1.get_users()))
        founder1 = FounderFactory()
        self.company1.founders.add(founder1)
        self.assertEqual(1, len(self.company1.get_users()))
        users = self.company1.get_users()
        self.assertEqual(founder1.user, users[0])
