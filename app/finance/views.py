# coding: utf-8

from django.shortcuts import render, redirect
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from app.company.models import Company
from app.finance.models import Bourse, Subvention, Investissement, Pret, Vente
from app.founder.models import Founder
from app.mentor.models import Mentor

#The general view
class detailFinance(generic.TemplateView):

    template_name = 'finance/index.html'

    #You need to be connected, and you need to have access as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    company = Company.objects.get(id = int(self.args[0])) #If the company exist, else we go to except
                    return super(detailFinance, self).dispatch(*args, **kwargs)
                except:
                    pass

        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(int(self.args[0]) == int(company.id)):
                    return super(detailFinance, self).dispatch(*args, **kwargs)
            except:
                pass

        #For know the company of the user if is a mentor
        if self.request.user.is_active:
            try:
                mentor = Mentor.objects.filter(user = self.request.user.id)
                company = Company.objects.get(mentors = mentor)
                if(int(self.args[0]) == int(company.id)):
                    return super(detailFinance, self).dispatch(*args, **kwargs)
            except:
                pass

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        company = Company.objects.get(id = self.args[0])
        bourses = Bourse.objects.filter(company = company).order_by('dateSoumission')
        subventions = Subvention.objects.filter(company = company).order_by('dateSoumission')
        investissements = Investissement.objects.filter(company = company).order_by('dateSoumission')
        prets = Pret.objects.filter(company = company).order_by('dateSoumission')
        ventes = Vente.objects.filter(company = company).order_by('dateSoumission')

        totalBoursesSoumises = 0
        for bourse in bourses:
            try:
                totalBoursesSoumises += bourse.sommeSoumission
            except:
                pass

        totalBoursesRecues = 0
        for bourse in bourses:
            try:
                totalBoursesRecues += bourse.sommeReception
            except:
                pass

        totalSubventionsSoumises = 0
        for subvention in subventions:
            try:
                totalSubventionsSoumises += subvention.sommeSoumission
            except:
                pass

        totalSubventionsRecues = 0
        for subvention in subventions:
            try:
                totalSubventionsRecues += subvention.sommeReception
            except:
                pass

        totalInvestissementsSoumis = 0
        for investissement in investissements:
            try:
                totalInvestissementsSoumis += investissement.sommeSoumission
            except:
                pass

        totalInvestissementsRecus = 0
        for investissement in investissements:
            try:
                totalInvestissementsRecus += investissement.sommeReception
            except:
                pass

        totalPretsSoumis = 0
        for pret in prets:
            try:
                totalPretsSoumis += pret.sommeSoumission
            except:
                pass

        totalPretsRecus = 0
        for pret in prets:
            try:
                totalPretsRecus += pret.sommeReception
            except:
                pass
        totalVentesSoumises = 0
        for vente in ventes:
            try:
                totalVentesSoumises += vente.sommeSoumission
            except:
                pass

        totalVentesRecues = 0
        for vente in ventes:
            try:
                totalVentesRecues += vente.sommeReception
            except:
                pass

        context = super(detailFinance, self).get_context_data(**kwargs)

        isFounder = False
        listFounder = Founder.objects.filter(company__pk = self.args[0])
        for founder in listFounder:
            if founder.user.id == self.request.user.id:
                isFounder = True
        context['isFounder'] = isFounder

        context['company'] = company
        context['bourses'] = bourses
        context['subventions'] = subventions
        context['investissements'] = investissements
        context['prets'] = prets
        context['ventes'] = ventes
        context['totalBoursesSoumises'] = totalBoursesSoumises
        context['totalBoursesRecues'] = totalBoursesRecues
        context['totalSubventionsSoumises'] = totalSubventionsSoumises
        context['totalSubventionsRecues'] = totalSubventionsRecues
        context['totalInvestissementsSoumis'] = totalInvestissementsSoumis
        context['totalInvestissementsRecus'] = totalInvestissementsRecus
        context['totalPretsSoumis'] = totalPretsSoumis
        context['totalPretsRecus'] = totalPretsRecus
        context['totalVentesSoumises'] = totalVentesSoumises
        context['totalVentesRecues'] = totalVentesRecues
        return context

#For create a new grants
class BourseCreate(generic.CreateView):
    model = Bourse
    fields = ['name','dateSoumission','sommeSoumission','dateReception',
              'sommeReception','description']

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    company = Company.objects.get(id = int(self.args[0])) #If the company exist, else we go to except
                    return super(BourseCreate, self).dispatch(*args, **kwargs)
                except:
                    pass

        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(int(self.args[0]) == int(company.id)):
                    return super(BourseCreate, self).dispatch(*args, **kwargs)
            except:
                pass

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def form_valid(self, form):
         company = Company.objects.get(id = self.args[0])
         form.instance.company = company
         return super(BourseCreate, self).form_valid(form)

#For update a grants
class BourseUpdate(generic.UpdateView):
    model = Bourse
    fields = ['name','dateSoumission','sommeSoumission','dateReception',
              'sommeReception','description']

    def get_url(self):
        self.object = self.get_object()
        return reverse_lazy('finance:detail_finance', kwargs = {'companyId' : self.object.company.id, })

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    self.object = self.get_object()
                    company = Company.objects.get(id = self.object.company.id) #If the company exist, else we go to except
                    return super(BourseUpdate, self).dispatch(*args, **kwargs)
                except:
                    pass

        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                self.object = self.get_object()
                company_id = self.object.company.id
                if(int(company_id) == int(company.id)):
                    return super(BourseUpdate, self).dispatch(*args, **kwargs)
            except:
                pass
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

#For delete a grants
class BourseDelete(generic.DeleteView):
    model = Bourse

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    self.object = self.get_object()
                    company = Company.objects.get(id = self.object.company.id) #If the company exist, else we go to except
                    return super(BourseDelete, self).dispatch(*args, **kwargs)
                except:
                    pass


        #For know the company of the user if is a founder
        if self.request.user.is_active:
             try:
                founder = Founder.objects.filter(user = self.request.user.id)

                company = Company.objects.get(founders = founder)
                bourse = Bourse.objects.get(id = kwargs['pk'])

                company_id = bourse.company.id
                if(int(company_id) == int(company.id)):
                    return super(BourseDelete, self).dispatch(*args, **kwargs)
             except:
                #The visitor can't see this page!
                return HttpResponseRedirect("/user/noAccessPermissions")
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(BourseDelete, self).get_context_data(**kwargs)
        context['companyId'] = kwargs['object'].company.id
        context['bourse'] = kwargs['object']
        return context

    #rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy('finance:detail_finance', args = {company_id}))

#For create a new Subsidy
class SubventionCreate(generic.CreateView):
    model = Subvention
    fields = ['name','dateSoumission','sommeSoumission','dateReception',
              'sommeReception','description']

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    company = Company.objects.get(id = int(self.args[0])) #If the company exist, else we go to except
                    return super(SubventionCreate, self).dispatch(*args, **kwargs)
                except:
                    pass

        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(int(self.args[0]) == int(company.id)):
                    return super(SubventionCreate, self).dispatch(*args, **kwargs)
            except:
                pass

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def form_valid(self, form):
         company = Company.objects.get(id = self.args[0])
         form.instance.company = company
         return super(SubventionCreate, self).form_valid(form)

#For update a Subsidy
class SubventionUpdate(generic.UpdateView):
    model = Subvention
    fields = ['name','dateSoumission','sommeSoumission','dateReception',
              'sommeReception','description']

    def get_url(self):
        self.object = self.get_object()
        return reverse_lazy('finance:detail_finance', kwargs = {'companyId' : self.object.company.id, })

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    self.object = self.get_object()
                    company = Company.objects.get(id = self.object.company.id) #If the company exist, else we go to except
                    return super(SubventionUpdate, self).dispatch(*args, **kwargs)
                except:
                    pass

        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                self.object = self.get_object()
                company_id = self.object.company.id
                if(int(company_id) == int(company.id)):
                    return super(SubventionUpdate, self).dispatch(*args, **kwargs)
            except:
                pass
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

#For delete a Subsidy
class SubventionDelete(generic.DeleteView):
    model = Subvention

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    self.object = self.get_object()
                    company = Company.objects.get(id = self.object.company.id) #If the company exist, else we go to except
                    return super(SubventionDelete, self).dispatch(*args, **kwargs)
                except:
                    pass


        #For know the company of the user if is a founder
        if self.request.user.is_active:
             try:
                founder = Founder.objects.filter(user = self.request.user.id)

                company = Company.objects.get(founders = founder)
                subvention = Subvention.objects.get(id = kwargs['pk'])

                company_id = subvention.company.id
                if(int(company_id) == int(company.id)):
                    return super(SubventionDelete, self).dispatch(*args, **kwargs)
             except:
                pass
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(SubventionDelete, self).get_context_data(**kwargs)
        context['companyId'] = kwargs['object'].company.id
        context['subvention'] = kwargs['object']
        return context

    #rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy('finance:detail_finance', args = {company_id}))

#For create a new Investment
class InvestissementCreate(generic.CreateView):
    model = Investissement
    fields = ['name','dateSoumission','sommeSoumission','dateReception',
              'sommeReception','description']

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    company = Company.objects.get(id = int(self.args[0])) #If the company exist, else we go to except
                    return super(InvestissementCreate, self).dispatch(*args, **kwargs)
                except:
                    pass

        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(int(self.args[0]) == int(company.id)):
                    return super(InvestissementCreate, self).dispatch(*args, **kwargs)
            except:
                pass

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def form_valid(self, form):
         company = Company.objects.get(id = self.args[0])
         form.instance.company = company
         return super(InvestissementCreate, self).form_valid(form)

#For update an Investment
class InvestissementUpdate(generic.UpdateView):
    model = Investissement
    fields = ['name','dateSoumission','sommeSoumission','dateReception',
              'sommeReception','description']

    def get_url(self):
        return reverse_lazy('finance:detail_finance', kwargs = {'companyId' : self.args[0], })

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    self.object = self.get_object()
                    company = Company.objects.get(id = self.object.company.id) #If the company exist, else we go to except
                    return super(InvestissementUpdate, self).dispatch(*args, **kwargs)
                except:
                    pass


        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                self.object = self.get_object()
                company_id = self.object.company.id
                if(int(company_id) == int(company.id)):
                    return super(InvestissementUpdate, self).dispatch(*args, **kwargs)
            except:
                pass
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

#For delete an Investment
class InvestissementDelete(generic.DeleteView):
    model = Investissement

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    self.object = self.get_object()
                    company = Company.objects.get(id = self.object.company.id) #If the company exist, else we go to except
                    return super(InvestissementDelete, self).dispatch(*args, **kwargs)
                except:
                    pass


        #For know the company of the user if is a founder
        if self.request.user.is_active:
             try:
                founder = Founder.objects.filter(user = self.request.user.id)

                company = Company.objects.get(founders = founder)
                investissement = Investissement.objects.get(id = kwargs['pk'])

                company_id = investissement.company.id
                if(int(company_id) == int(company.id)):
                    return super(InvestissementDelete, self).dispatch(*args, **kwargs)
             except:
                pass
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(InvestissementDelete, self).get_context_data(**kwargs)
        context['companyId'] = kwargs['object'].company.id
        context['subvention'] = kwargs['object']
        return context

    #rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy('finance:detail_finance', args = {company_id}))

#For create a new Loans
class PretCreate(generic.CreateView):
    model = Pret
    fields = ['name','dateSoumission','sommeSoumission','dateReception',
              'sommeReception','description']

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    company = Company.objects.get(id = int(self.args[0])) #If the company exist, else we go to except
                    return super(PretCreate, self).dispatch(*args, **kwargs)
                except:
                    pass

        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(int(self.args[0]) == int(company.id)):
                    return super(PretCreate, self).dispatch(*args, **kwargs)
            except:
                pass

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def form_valid(self, form):
         company = Company.objects.get(id = self.args[0])
         form.instance.company = company
         return super(PretCreate, self).form_valid(form)

#For update a Loans
class PretUpdate(generic.UpdateView):
    model = Pret
    fields = ['name','dateSoumission','sommeSoumission','dateReception',
              'sommeReception','description']

    def get_url(self):
        return reverse_lazy('finance:detail_finance', kwargs = {'companyId' : self.args[0], })

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    self.object = self.get_object()
                    company = Company.objects.get(id = self.object.company.id) #If the company exist, else we go to except
                    return super(PretUpdate, self).dispatch(*args, **kwargs)
                except:
                    pass


        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                self.object = self.get_object()
                company_id = self.object.company.id
                if(int(company_id) == int(company.id)):
                    return super(PretUpdate, self).dispatch(*args, **kwargs)
            except:
                pass
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

#For delete a Loans
class PretDelete(generic.DeleteView):
    model = Pret

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    self.object = self.get_object()
                    company = Company.objects.get(id = self.object.company.id) #If the company exist, else we go to except
                    return super(PretDelete, self).dispatch(*args, **kwargs)
                except:
                    pass


        #For know the company of the user if is a founder
        if self.request.user.is_active:
             try:
                founder = Founder.objects.filter(user = self.request.user.id)

                company = Company.objects.get(founders = founder)
                pret = Pret.objects.get(id = kwargs['pk'])

                company_id = pret.company.id
                if(int(company_id) == int(company.id)):
                    return super(PretDelete, self).dispatch(*args, **kwargs)
             except:
                pass
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(PretDelete, self).get_context_data(**kwargs)
        context['companyId'] = kwargs['object'].company.id
        context['subvention'] = kwargs['object']
        return context

    #rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy('finance:detail_finance', args = {company_id}))

#For create a new Sale
class VenteCreate(generic.CreateView):
    model = Vente
    fields = ['name','dateSoumission','sommeSoumission','dateReception',
              'sommeReception','description']

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    company = Company.objects.get(id = int(self.args[0])) #If the company exist, else we go to except
                    return super(VenteCreate, self).dispatch(*args, **kwargs)
                except:
                    pass

        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(int(self.args[0]) == int(company.id)):
                    return super(VenteCreate, self).dispatch(*args, **kwargs)
            except:
                pass

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def form_valid(self, form):
         company = Company.objects.get(id = self.args[0])
         form.instance.company = company
         return super(VenteCreate, self).form_valid(form)

#For update a Sale
class VenteUpdate(generic.UpdateView):
    model = Vente
    fields = ['name','dateSoumission','sommeSoumission','dateReception',
              'sommeReception','description']

    def get_url(self):
        return reverse_lazy('finance:detail_finance', kwargs = {'companyId' : self.args[0], })

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    self.object = self.get_object()
                    company = Company.objects.get(id = self.object.company.id) #If the company exist, else we go to except
                    return super(VenteUpdate, self).dispatch(*args, **kwargs)
                except:
                    pass


        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                self.object = self.get_object()
                company_id = self.object.company.id
                if(int(company_id) == int(company.id)):
                    return super(VenteUpdate, self).dispatch(*args, **kwargs)
            except:
                pass
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

#For delete a Sale
class VenteDelete(generic.DeleteView):
    model = Vente

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    self.object = self.get_object()
                    company = Company.objects.get(id = self.object.company.id) #If the company exist, else we go to except
                    return super(VenteDelete, self).dispatch(*args, **kwargs)
                except:
                    pass


        #For know the company of the user if is a founder
        if self.request.user.is_active:
             try:
                founder = Founder.objects.filter(user = self.request.user.id)

                company = Company.objects.get(founders = founder)
                vente = Vente.objects.get(id = kwargs['pk'])

                company_id = vente.company.id
                if(int(company_id) == int(company.id)):
                    return super(VenteDelete, self).dispatch(*args, **kwargs)
             except:
                pass
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(VenteDelete, self).get_context_data(**kwargs)
        context['companyId'] = kwargs['object'].company.id
        context['subvention'] = kwargs['object']
        return context

    #rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy('finance:detail_finance', args = {company_id}))
