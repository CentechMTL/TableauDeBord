# coding: utf-8

import factory

from app.experiment.models import CustomerExperiment
from app.company.factories import CompanyFactory


class CustomerExperimentFactory(factory.DjangoModelFactory):
    class Meta:
        model = CustomerExperiment

    @classmethod
    def __init__(self, **kwargs):
        hypothesis = kwargs.pop('hypothesis', None)
        experiment_description = kwargs.pop('description', None)
        test_subject_count = kwargs.pop('subject_count', None)
        test_subject_description = kwargs.pop('subject_description', None)
        company = kwargs.pop('company', None)

        experiment = super(CustomerExperimentFactory, self).\
            __init__(self, **kwargs)

        experiment.save()
