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

#Display all experiment of a company
class CustomerExperimentList(generic.ListView):
    model = CustomerExperiment

    #You need to be connected, and you need to have access as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    company = Company.objects.get(id = int(self.args[0])) #If the company exist, else we go to except
                    return super(CustomerExperimentList, self).dispatch(*args, **kwargs)
                except:
                    pass

        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(int(self.args[0]) == int(company.id)):
                    return super(CustomerExperimentList, self).dispatch(*args, **kwargs)
            except:
                pass

        #For know the company of the user if is a mentor
        if self.request.user.is_active:
            try:
                mentor = Mentor.objects.filter(user = self.request.user.id)
                company = Company.objects.get(mentors = mentor)
                if(int(self.args[0]) == int(company.id)):
                    return super(CustomerExperimentList, self).dispatch(*args, **kwargs)
            except:
                pass

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_queryset(self):
        return CustomerExperiment.objects.filter(company = self.args[0])

    def get_context_data(self, **kwargs):
        context = super(CustomerExperimentList, self).get_context_data(**kwargs)
        isFounder = False
        listFounder = Founder.objects.filter(company__pk = self.args[0])
        for founder in listFounder:
            if founder.user.id == self.request.user.id:
                isFounder = True
        context['companyId'] = self.args[0]
        context['isFounder'] = isFounder
        return context

#Create an experiment
class CustomerExperimentCreate(CreateView):
    model = CustomerExperiment
    fields = ['validated','hypothesis','experiment_description','test_subject_count',
              'test_subject_description','conclusions']

    #You need to be connected, and you need to have access as founder only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(int(self.args[0]) == int(company.id)):
                    return super(CustomerExperimentCreate, self).dispatch(*args, **kwargs)
            except:
                #The visitor can't see this page!
                return HttpResponseRedirect("/user/noAccessPermissions")
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def form_valid(self, form):
         company = Company.objects.get(id = self.args[0])
         form.instance.company = company
         return super(CustomerExperimentCreate, self).form_valid(form)

#Update an experiment
class CustomerExperimentUpdate(UpdateView):
    model = CustomerExperiment
    fields = ['validated','hypothesis','experiment_description','test_subject_count',
              'test_subject_description','conclusions']

    def get_url(self):
        return reverse_lazy('experiment_list', kwargs = {'companyId' : self.args[0], })

    #You need to be connected, and you need to have access as founder only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                self.object = self.get_object()
                company_id = self.object.company.id
                if(int(company_id) == int(company.id)):
                    return super(CustomerExperimentUpdate, self).dispatch(*args, **kwargs)
            except:
                #The visitor can't see this page!
                return HttpResponseRedirect("/user/noAccessPermissions")
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

#Delete an experiment
class CustomerExperimentDelete(DeleteView):
    model = CustomerExperiment

    #You need to be connected, and you need to have access as founder only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know the company of the user if is a founder
        if self.request.user.is_active:
             try:
                founder = Founder.objects.filter(user = self.request.user.id)

                company = Company.objects.get(founders = founder)
                customerExperiment = CustomerExperiment.objects.get(id = kwargs['pk'])

                company_id = customerExperiment.company.id
                if(int(company_id) == int(company.id)):
                    return super(CustomerExperimentDelete, self).dispatch(*args, **kwargs)
             except:
                #The visitor can't see this page!
                return HttpResponseRedirect("/user/noAccessPermissions")
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(CustomerExperimentDelete, self).get_context_data(**kwargs)
        context['companyId'] = kwargs['object'].company.id
        context['experiment'] = kwargs['object']
        return context

    #rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy('experiment_list', args = {company_id}))
