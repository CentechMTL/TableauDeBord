# coding: utf-8

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from app.company.models import Company
from app.finance.models import Bourse, Subvention, Investissement, Pret, Vente
from app.founder.models import Founder
from app.mentor.models import Mentor
from app.finance.forms import FinanceForm, FinanceCreateForm
from django.contrib import messages

#The general view
class detailFinance(generic.TemplateView):

    template_name = 'finance/index.html'

    #You need to be connected, and you need to have access as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        company = get_object_or_404(Company, id = int(self.args[0]))

        if self.request.user.profile.isCentech():
            return super(detailFinance, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(detailFinance, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isMentor():
            if company in self.request.user.profile.isMentor().company.all():
                return super(detailFinance, self).dispatch(*args, **kwargs)

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
    template_name = 'finance/bourse_form.html'
    form_class = FinanceCreateForm

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        company = get_object_or_404(Company, id = int(self.args[0]))

        if self.request.user.profile.isCentech():
            return super(BourseCreate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(BourseCreate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self, form_class):
        return form_class()

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.create_object(form)
            messages.success(self.request, self.get_success_message())
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def create_object(self, form):
        company = Company.objects.get(id=self.args[0])
        name = form.data['name']
        sommeSoumission = form.data['sommeSoumission']
        dateSoumission = form.data['dateSoumission']
        sommeReception = form.data['sommeReception']
        dateReception = form.data['dateReception']
        description = form.data['description']

        newObject = Bourse(company=company,
                        name=name,
                        sommeSoumission=sommeSoumission,
                        dateSoumission=dateSoumission)
        newObject.save()
        self.object = newObject

        try:
            if(sommeReception):
                newObject.sommeReception = sommeReception
            if(dateReception):
                newObject.dateReception = dateReception
            if(description):
                newObject.description = description
        except:
            pass

        newObject.save()

    def get_success_url(self):
        return reverse_lazy('finance:detail_finance', args={self.object.company.id})

    def get_success_message(self):
        return (u'La bourse a bien été ajouté.')

#For update a grants
class BourseUpdate(generic.UpdateView):
    model = Bourse
    form_class = FinanceForm
    template_name = "finance/bourse_form.html"

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id = self.object.company.id)

        if self.request.user.profile.isCentech():
            return super(BourseUpdate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(BourseUpdate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self):
        self.form = self.form_class(self.get_object())
        return self.form

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        form = self.form_class(object, request.POST)
        if form.is_valid():
            print form.is_valid()
            self.update_object(object, form)
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def update_object(self, object, form):
        object.name = form.data['name']
        object.sommeSoumission = form.data['sommeSoumission']
        object.dateSoumission = form.data['dateSoumission']
        object.sommeReception = form.data['sommeReception']
        object.dateReception = form.data['dateReception']
        object.description = form.data['description']

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy('finance:detail_finance', args={self.object.company.id})

#For delete a grants
class BourseDelete(generic.DeleteView):
    model = Bourse

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id = self.object.company.id)

        if self.request.user.profile.isCentech():
            return super(BourseDelete, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                    return super(BourseDelete, self).dispatch(*args, **kwargs)

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
    template_name = 'finance/subvention_form.html'
    form_class = FinanceCreateForm

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        company = get_object_or_404(Company, id = self.args[0])

        if self.request.user.profile.isCentech():
            return super(SubventionCreate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(SubventionCreate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self, form_class):
        return form_class()

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.create_object(form)
            messages.success(self.request, self.get_success_message())
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def create_object(self, form):
        company = Company.objects.get(id=self.args[0])
        name = form.data['name']
        sommeSoumission = form.data['sommeSoumission']
        dateSoumission = form.data['dateSoumission']
        sommeReception = form.data['sommeReception']
        dateReception = form.data['dateReception']
        description = form.data['description']

        newObject = Subvention(company=company,
                        name=name,
                        sommeSoumission=sommeSoumission,
                        dateSoumission=dateSoumission)
        newObject.save()
        self.object = newObject

        try:
            if(sommeReception):
                newObject.sommeReception = sommeReception
            if(dateReception):
                newObject.dateReception = dateReception
            if(description):
                newObject.description = description
        except:
            pass

        newObject.save()

    def get_success_url(self):
        return reverse_lazy('finance:detail_finance', args={self.object.company.id})

    def get_success_message(self):
        return (u'La subvention a bien été ajouté.')

#For update a Subsidy
class SubventionUpdate(generic.UpdateView):
    model = Subvention
    form_class = FinanceForm
    template_name = "finance/subvention_form.html"

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id = self.object.company.id)

        if self.request.user.profile.isCentech():
            return super(SubventionUpdate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(SubventionUpdate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self):
        self.form = self.form_class(self.get_object())
        return self.form

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        form = self.form_class(object, request.POST)
        if form.is_valid():
            print form.is_valid()
            self.update_object(object, form)
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def update_object(self, object, form):
        object.name = form.data['name']
        object.sommeSoumission = form.data['sommeSoumission']
        object.dateSoumission = form.data['dateSoumission']
        object.sommeReception = form.data['sommeReception']
        object.dateReception = form.data['dateReception']
        object.description = form.data['description']

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy('finance:detail_finance', args={self.object.company.id})

#For delete a Subsidy
class SubventionDelete(generic.DeleteView):
    model = Subvention

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id = self.object.company.id)

        if self.request.user.profile.isCentech():
            return super(SubventionDelete, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(SubventionDelete, self).dispatch(*args, **kwargs)

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
    template_name = 'finance/investissement_form.html'
    form_class = FinanceCreateForm

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        company = get_object_or_404(Company, id = self.args[0])

        if self.request.user.profile.isCentech():
            return super(InvestissementCreate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                    return super(InvestissementCreate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self, form_class):
        return form_class()

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.create_object(form)
            messages.success(self.request, self.get_success_message())
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def create_object(self, form):
        company = Company.objects.get(id=self.args[0])
        name = form.data['name']
        sommeSoumission = form.data['sommeSoumission']
        dateSoumission = form.data['dateSoumission']
        sommeReception = form.data['sommeReception']
        dateReception = form.data['dateReception']
        description = form.data['description']

        newObject = Investissement(company=company,
                        name=name,
                        sommeSoumission=sommeSoumission,
                        dateSoumission=dateSoumission)
        newObject.save()
        self.object = newObject

        try:
            if(sommeReception):
                newObject.sommeReception = sommeReception
            if(dateReception):
                newObject.dateReception = dateReception
            if(description):
                newObject.description = description
        except:
            pass

        newObject.save()

    def get_success_url(self):
        return reverse_lazy('finance:detail_finance', args={self.object.company.id})

    def get_success_message(self):
        return (u'L\'investissement a bien été ajouté.')

#For update an Investment
class InvestissementUpdate(generic.UpdateView):
    model = Investissement
    form_class = FinanceForm
    template_name = "finance/investissement_form.html"

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()

        if self.request.user.profile.isCentech():
            return super(InvestissementUpdate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if self.request.user.profile.isFounder().company.all():
                return super(InvestissementUpdate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self):
        self.form = self.form_class(self.get_object())
        return self.form

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        form = self.form_class(object, request.POST)
        if form.is_valid():
            print form.is_valid()
            self.update_object(object, form)
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def update_object(self, object, form):
        object.name = form.data['name']
        object.sommeSoumission = form.data['sommeSoumission']
        object.dateSoumission = form.data['dateSoumission']
        object.sommeReception = form.data['sommeReception']
        object.dateReception = form.data['dateReception']
        object.description = form.data['description']

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy('finance:detail_finance', args={self.object.company.id})

#For delete an Investment
class InvestissementDelete(generic.DeleteView):
    model = Investissement

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id = self.object.company.id)

        if self.request.user.profile.isCentech():
            return super(InvestissementDelete, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(InvestissementDelete, self).dispatch(*args, **kwargs)

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
    template_name = 'finance/pret_form.html'
    form_class = FinanceCreateForm

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        company = get_object_or_404(Company, id = self.args[0])

        if self.request.user.profile.isCentech():
            return super(PretCreate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(PretCreate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self, form_class):
        return form_class()

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.create_object(form)
            messages.success(self.request, self.get_success_message())
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def create_object(self, form):
        company = Company.objects.get(id=self.args[0])
        name = form.data['name']
        sommeSoumission = form.data['sommeSoumission']
        dateSoumission = form.data['dateSoumission']
        sommeReception = form.data['sommeReception']
        dateReception = form.data['dateReception']
        description = form.data['description']

        newObject = Pret(company=company,
                        name=name,
                        sommeSoumission=sommeSoumission,
                        dateSoumission=dateSoumission)
        newObject.save()
        self.object = newObject

        try:
            if(sommeReception):
                newObject.sommeReception = sommeReception
            if(dateReception):
                newObject.dateReception = dateReception
            if(description):
                newObject.description = description
        except:
            pass

        newObject.save()

    def get_success_url(self):
        return reverse_lazy('finance:detail_finance', args={self.object.company.id})

    def get_success_message(self):
        return (u'Le pret a bien été ajouté.')

#For update a Loans
class PretUpdate(generic.UpdateView):
    model = Pret
    form_class = FinanceForm
    template_name = "finance/pret_form.html"

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id = self.object.company.id)

        if self.request.user.profile.isCentech():
            return super(PretUpdate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(PretUpdate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self):
        self.form = self.form_class(self.get_object())
        return self.form

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        form = self.form_class(object, request.POST)
        if form.is_valid():
            print form.is_valid()
            self.update_object(object, form)
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def update_object(self, object, form):
        object.name = form.data['name']
        object.sommeSoumission = form.data['sommeSoumission']
        object.dateSoumission = form.data['dateSoumission']
        object.sommeReception = form.data['sommeReception']
        object.dateReception = form.data['dateReception']
        object.description = form.data['description']

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy('finance:detail_finance', args={self.object.company.id})

#For delete a Loans
class PretDelete(generic.DeleteView):
    model = Pret

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id = self.object.company.id)

        if self.request.user.profile.isCentech():
            return super(PretDelete, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(PretDelete, self).dispatch(*args, **kwargs)

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
    template_name = 'finance/vente_form.html'
    form_class = FinanceCreateForm

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):

        company = get_object_or_404(Company, id = self.args[0])

        if self.request.user.profile.isCentech():
            return super(VenteCreate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(VenteCreate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self, form_class):
        return form_class()

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.create_object(form)
            messages.success(self.request, self.get_success_message())
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def create_object(self, form):
        company = Company.objects.get(id=self.args[0])
        name = form.data['name']
        sommeSoumission = form.data['sommeSoumission']
        dateSoumission = form.data['dateSoumission']
        sommeReception = form.data['sommeReception']
        dateReception = form.data['dateReception']
        description = form.data['description']

        newObject = Vente(company=company,
                        name=name,
                        sommeSoumission=sommeSoumission,
                        dateSoumission=dateSoumission)
        newObject.save()
        self.object = newObject

        try:
            if(sommeReception):
                newObject.sommeReception = sommeReception
            if(dateReception):
                newObject.dateReception = dateReception
            if(description):
                newObject.description = description
        except:
            pass

        newObject.save()

    def get_success_url(self):
        return reverse_lazy('finance:detail_finance', args={self.object.company.id})

    def get_success_message(self):
        return (u'La vente a bien été ajouté.')

#For update a Sale
class VenteUpdate(generic.UpdateView):
    model = Vente
    form_class = FinanceForm
    template_name = "finance/vente_form.html"

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id = self.object.company.id)

        if self.request.user.profile.isCentech():
            return super(VenteUpdate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(VenteUpdate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self):
        self.form = self.form_class(self.get_object())
        return self.form

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        form = self.form_class(object, request.POST)
        if form.is_valid():
            print form.is_valid()
            self.update_object(object, form)
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def update_object(self, object, form):
        object.name = form.data['name']
        object.sommeSoumission = form.data['sommeSoumission']
        object.dateSoumission = form.data['dateSoumission']
        object.sommeReception = form.data['sommeReception']
        object.dateReception = form.data['dateReception']
        object.description = form.data['description']

    def get_success_url(self, *args):
        self.object = self.get_object()
        return reverse_lazy('finance:detail_finance', args={self.object.company.id})

#For delete a Sale
class VenteDelete(generic.DeleteView):
    model = Vente

    #You need to be connected, and you need to have access as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id = self.object.company.id)

        if self.request.user.profile.isCentech():
            return super(VenteDelete, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if self.request.user.profile.isFounder().company.all():
                return super(VenteDelete, self).dispatch(*args, **kwargs)

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
