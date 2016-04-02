from django.test import TestCase
import datetime

from app.company.factories import CompanyStatusFactory, CompanyFactory
from app.kanboard.factories import CardFactory
from app.kanboard.models import PHASE_CHOICES


class CardModelsTest(TestCase):

    def setUp(self):
        self.status1 = CompanyStatusFactory()
        self.company1 = CompanyFactory(companyStatus=self.status1)

        self.card1 = CardFactory(company=self.company1,
                                 phase=PHASE_CHOICES[1][1],
                                 state=False)

    def test_is_past_due(self):
        self.assertEqual(False, self.card1.is_past_due())
        self.card1.deadline = datetime.date.today()
        self.assertEqual(False, self.card1.is_past_due())
        self.card1.deadline = datetime.date(2015, 01, 01)
        self.assertEqual(True, self.card1.is_past_due())

    def test_change_phase(self):
        self.card1.change_phase(PHASE_CHOICES[0][1])
        self.assertEqual(PHASE_CHOICES[0][1], self.card1.phase)
        self.card1.change_phase(PHASE_CHOICES[1][1])
        self.assertEqual(PHASE_CHOICES[1][1], self.card1.phase)
