# coding: utf-8
from django.test import TestCase

from app.company.factories import CompanyStatusFactory
from app.home.factories import StaffUserFactory

from app.company.forms import CompanyCreateForm, CompanyUpdateForm, CompanyStatusCreateForm

class CompanyStatusCreateFormTest(TestCase):
    """
    Check the form to create a status of company.
    """

    def test_valid(self):
        data = {
            'name': 'Tester'
        }

        form = CompanyStatusCreateForm(data=data)
        self.assertTrue(form.is_valid())

    def test_missing_name(self):
        data = {
        }
        form = CompanyStatusCreateForm(data=data)
        self.assertFalse(form.is_valid())