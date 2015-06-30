# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from app.kpi.models import KPI, KPI_TYPE_CHOICES
from app.company.models import Company
from app.founder.models import Founder
from app.mentor.models import Mentor
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect

#Display TRL of a company
class trl(TemplateView):
    template_name = 'kpi/trl.html'

    #You need to be connected, and you need to have access as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    company = Company.objects.get(id = int(self.args[0])) #If the company exist, else we go to except
                    return super(trl, self).dispatch(*args, **kwargs)
                except:
                    pass

        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(int(self.args[0]) == int(company.id)):
                    return super(trl, self).dispatch(*args, **kwargs)
            except:
                pass

        #For know the company of the user if is a mentor
        if self.request.user.is_active:
            try:
                mentor = Mentor.objects.filter(user = self.request.user.id)
                company = Company.objects.get(mentors = mentor)
                if(int(self.args[0]) == int(company.id)):
                    return super(trl, self).dispatch(*args, **kwargs)
            except:
                pass

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        company = Company.objects.get(id = self.args[0])
        idType = KPI_TYPE_CHOICES[1][0]
        trls = KPI.objects.filter(company = self.args[0], type=idType).order_by('period_start')
        nbTrl = trls.count
        context = super(trl, self).get_context_data(**kwargs)
        context['company'] = company
        context['trls'] = trls
        context['nbTrl'] = nbTrl
        return context

#Display IRL of a company
class irl(TemplateView):
    template_name = 'kpi/irl.html'

   #You need to be connected, and you need to have access as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    company = Company.objects.get(id = int(self.args[0])) #If the company exist, else we go to except
                    return super(irl, self).dispatch(*args, **kwargs)
                except:
                    pass

        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(int(self.args[0]) == int(company.id)):
                    return super(irl, self).dispatch(*args, **kwargs)
            except:
                pass

        #For know the company of the user if is a mentor
        if self.request.user.is_active:
            try:
                mentor = Mentor.objects.filter(user = self.request.user.id)
                company = Company.objects.get(mentors = mentor)
                if(int(self.args[0]) == int(company.id)):
                    return super(irl, self).dispatch(*args, **kwargs)
            except:
                pass

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        company = Company.objects.get(id = self.args[0])
        idType = KPI_TYPE_CHOICES[0][0]
        irls = KPI.objects.filter(company = self.args[0], type=idType).order_by('period_start')
        nbIrl = irls.count
        context = super(irl, self).get_context_data(**kwargs)
        context['company'] = company
        context['irls'] = irls
        context['nbIrl'] = nbIrl
        return context

class IrlCreate(CreateView):
    model = KPI
    template_name = 'kpi/irl_form.html'
    fields = ['level', 'comment']

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return super(IrlCreate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def form_valid(self, form):
         company = Company.objects.get(id = self.args[0])
         type = KPI_TYPE_CHOICES[0][0]
         form.instance.company = company
         form.instance.phase = company.companyStatus
         form.instance.type = type
         return super(IrlCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        company = Company.objects.get(id = self.args[0])
        context = super(IrlCreate, self).get_context_data(**kwargs)
        context['company'] = company
        return context

class TrlCreate(CreateView):
    model = KPI
    template_name = 'kpi/trl_form.html'
    fields = ['level', 'comment']

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return super(TrlCreate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def form_valid(self, form):
         company = Company.objects.get(id = self.args[0])
         type = KPI_TYPE_CHOICES[1][0]
         form.instance.company = company
         form.instance.phase = company.companyStatus
         form.instance.type = type
         return super(TrlCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        company = Company.objects.get(id = self.args[0])
        context = super(TrlCreate, self).get_context_data(**kwargs)
        context['company'] = company
        return context

#Update an experiment
class IrlUpdate(UpdateView):
    model = KPI
    template_name = 'kpi/irl_form.html'
    fields = ['level','comment']

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                print('toto')
                return super(IrlUpdate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

#Delete an experiment
class IrlDelete(DeleteView):
    model = KPI
    template_name = 'kpi/irl_confirm_delete.html'

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return super(IrlDelete, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(IrlDelete, self).get_context_data(**kwargs)
        context['companyId'] = kwargs['object'].company.id
        context['irl'] = kwargs['object']
        return context

    #rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy('kpi:irl_filter', args = {company_id}))

#Update an experiment
class TrlUpdate(UpdateView):
    model = KPI
    template_name = 'kpi/trl_form.html'
    fields = ['level','comment']

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return super(TrlUpdate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

#Delete an experiment
class TrlDelete(DeleteView):
    model = KPI
    template_name = 'kpi/trl_confirm_delete.html'

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return super(TrlDelete, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(TrlDelete, self).get_context_data(**kwargs)
        context['companyId'] = kwargs['object'].company.id
        context['trl'] = kwargs['object']
        return context

    #rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy('kpi:trl_filter', args = {company_id}))
