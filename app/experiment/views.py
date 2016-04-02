# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from app.experiment.models import CustomerExperiment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from app.company.models import Company
from app.founder.models import Founder
from app.mentor.models import Mentor
from django.http import HttpResponseRedirect


# Display all experiment of a company
class CustomerExperimentList(generic.ListView):
    model = CustomerExperiment

    # You need to be connected, and you need to have access as founder, mentor
    # or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        company = get_object_or_404(Company, id=self.args[0])

        if self.request.user.profile.isCentech():
            return super(CustomerExperimentList, self).\
                dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(CustomerExperimentList, self).\
                    dispatch(*args, **kwargs)

        if self.request.user.profile.isMentor():
            if company in self.request.user.profile.isMentor().company.all():
                return super(CustomerExperimentList, self).\
                    dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_queryset(self):
        return CustomerExperiment.objects.filter(company=self.args[0])

    def get_context_data(self, **kwargs):
        context = super(CustomerExperimentList,
                        self).get_context_data(**kwargs)
        isFounder = False
        listFounder = Founder.objects.filter(company__pk=self.args[0])
        for founder in listFounder:
            if founder.user.id == self.request.user.id:
                isFounder = True
        context['company_id'] = self.args[0]
        context['company'] = Company.objects.get(id=self.args[0])
        context['is_founder'] = isFounder
        return context


# Create an experiment
class CustomerExperimentCreate(CreateView):
    model = CustomerExperiment
    fields = [
        'validated',
        'hypothesis',
        'experiment_description',
        'test_subject_count',
        'test_subject_description',
        'conclusions'
    ]

    # You need to be connected, and you need to have access as founder only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        company = get_object_or_404(Company, id=self.args[0])

        if self.request.user.profile.isFounder():
            if self.request.user.profile.isFounder().company.all():
                return super(CustomerExperimentCreate, self).\
                    dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def form_valid(self, form):
        company = Company.objects.get(id=self.args[0])
        form.instance.company = company
        return super(CustomerExperimentCreate, self).form_valid(form)


# Update an experiment
class CustomerExperimentUpdate(UpdateView):
    model = CustomerExperiment
    fields = [
        'validated',
        'hypothesis',
        'experiment_description',
        'test_subject_count',
        'test_subject_description',
        'conclusions'
    ]

    def get_url(self):
        return reverse_lazy(
            'experiment:experiment_list',
            kwargs={'companyId': self.args[0], }
        )

    # You need to be connected, and you need to have access as founder only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id=self.object.company.id)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().\
                    company.all():
                return super(CustomerExperimentUpdate, self).\
                    dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")


# Delete an experiment
class CustomerExperimentDelete(DeleteView):
    model = CustomerExperiment

    # You need to be connected, and you need to have access as founder only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id=self.object.company.id)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.\
                    isFounder().company.all():
                return super(CustomerExperimentDelete, self).\
                    dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(CustomerExperimentDelete, self).\
            get_context_data(**kwargs)
        context['company_id'] = kwargs['object'].company.id
        context['experiment'] = kwargs['object']
        return context

    # rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy(
            'experiment:experiment_list',
            args={company_id}
        ))
