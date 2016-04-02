# coding: utf-8

from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from app.company.models import Company
from app.finance.models import Bourse, Subvention, Investissement, Pret, Vente
from app.founder.models import Founder
from app.finance.forms import BourseForm, SubventionForm, InvestissementForm, \
    PretForm, VenteForm
from django.contrib import messages


class detailFinance(generic.TemplateView):
    # The general view
    template_name = 'finance/index.html'

    # You need to be connected, and you need to have access
    # as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        company = get_object_or_404(Company, id=int(self.args[0]))

        if self.request.user.profile.isCentech():
            return super(detailFinance, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(detailFinance, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isMentor():
            if company in self.request.user.profile.isMentor().company.all():
                return super(detailFinance, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        company = Company.objects.get(id=self.args[0])
        bourses = Bourse.objects.\
            filter(company=company).order_by('dateSoumission')
        subventions = Subvention.objects.\
            filter(company=company).order_by('dateSoumission')
        investissements = Investissement.objects.\
            filter(company=company).order_by('dateSoumission')
        prets = Pret.objects.filter(company=company).\
            order_by('dateSoumission')
        ventes = Vente.objects.filter(company=company).\
            order_by('dateSoumission')

        total_bourses_soumises = 0
        for bourse in bourses:
            try:
                total_bourses_soumises += bourse.somme_soumission
            except:
                pass

        total_bourses_recues = 0
        for bourse in bourses:
            try:
                total_bourses_recues += bourse.somme_reception
            except:
                pass

        total_subventions_soumises = 0
        for subvention in subventions:
            try:
                total_subventions_soumises += subvention.sommeSoumission
            except:
                pass

        total_subventions_recues = 0
        for subvention in subventions:
            try:
                total_subventions_recues += subvention.sommeReception
            except:
                pass

        total_investissements_soumis = 0
        for investissement in investissements:
            try:
                total_investissements_soumis += investissement.sommeSoumission
            except:
                pass

        total_investissements_recus = 0
        for investissement in investissements:
            try:
                total_investissements_recus += investissement.sommeReception
            except:
                pass

        total_prets_soumis = 0
        for pret in prets:
            try:
                total_prets_soumis += pret.sommeSoumission
            except:
                pass

        total_prets_recus = 0
        for pret in prets:
            try:
                total_prets_recus += pret.sommeReception
            except:
                pass
        total_ventes_soumises = 0
        for vente in ventes:
            try:
                total_ventes_soumises += vente.sommeSoumission
            except:
                pass

        total_ventes_recues = 0
        for vente in ventes:
            try:
                total_ventes_recues += vente.sommeReception
            except:
                pass

        context = super(detailFinance, self).get_context_data(**kwargs)

        is_founder = False
        list_founder = Founder.objects.filter(company__pk=self.args[0])
        for founder in list_founder:
            if founder.user.id == self.request.user.id:
                is_founder = True
        context['isFounder'] = is_founder

        context['company'] = company
        context['bourses'] = bourses
        context['subventions'] = subventions
        context['investissements'] = investissements
        context['prets'] = prets
        context['ventes'] = ventes
        context['totalBoursesSoumises'] = total_bourses_soumises
        context['totalBoursesRecues'] = total_bourses_recues
        context['totalSubventionsSoumises'] = total_subventions_soumises
        context['totalSubventionsRecues'] = total_subventions_recues
        context['totalInvestissementsSoumis'] = total_investissements_soumis
        context['totalInvestissementsRecus'] = total_investissements_recus
        context['totalPretsSoumis'] = total_prets_soumis
        context['totalPretsRecus'] = total_prets_recus
        context['totalVentesSoumises'] = total_ventes_soumises
        context['totalVentesRecues'] = total_ventes_recues
        return context


class BourseCreate(generic.CreateView):
    # For create a new grants
    model = Bourse
    template_name = 'finance/finance_form.html'
    form_class = BourseForm

    # You need to be connected, and you need to have access
    # as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        company = get_object_or_404(Company, id=int(self.args[0]))

        if self.request.user.profile.isCentech():
            return super(BourseCreate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(BourseCreate, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def form_valid(self, form):
        form.instance.company = Company.objects.get(id=int(self.args[0]))
        return super(BourseCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'finance:detail_finance',
            args={self.object.company.id}
        )


class BourseUpdate(generic.UpdateView):
    # For update a grants
    model = Bourse
    form_class = BourseForm
    template_name = "finance/finance_form.html"

    # You need to be connected, and you need to have access
    # as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id=self.object.company.id)

        if self.request.user.profile.isCentech():
            return super(BourseUpdate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(BourseUpdate, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy(
            'finance:detail_finance',
            args={self.object.company.id}
        )


class BourseDelete(generic.DeleteView):
    # For delete a grants
    model = Bourse

    # You need to be connected, and you need to have access
    # as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id=self.object.company.id)

        if self.request.user.profile.isCentech():
            return super(BourseDelete, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                    return super(BourseDelete, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(BourseDelete, self).get_context_data(**kwargs)
        context['companyId'] = kwargs['object'].company.id
        context['bourse'] = kwargs['object']
        return context

    # rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy(
            'finance:detail_finance',
            args={company_id}
        ))


class SubventionCreate(generic.CreateView):
    # For create a new Subsidy
    model = Subvention
    template_name = 'finance/finance_form.html'
    form_class = SubventionForm

    # You need to be connected, and you need to have access
    # as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        company = get_object_or_404(Company, id=self.args[0])

        if self.request.user.profile.isCentech():
            return super(SubventionCreate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(SubventionCreate, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def form_valid(self, form):
        form.instance.company = Company.objects.get(id=int(self.args[0]))
        return super(SubventionCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'finance:detail_finance',
            args={self.object.company.id}
        )


class SubventionUpdate(generic.UpdateView):
    # For update a Subsidy
    model = Subvention
    form_class = SubventionForm
    template_name = "finance/finance_form.html"

    # You need to be connected, and you need to have access
    # as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id=self.object.company.id)

        if self.request.user.profile.isCentech():
            return super(SubventionUpdate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(SubventionUpdate, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy(
            'finance:detail_finance',
            args={self.object.company.id}
        )


class SubventionDelete(generic.DeleteView):
    # For delete a Subsidy
    model = Subvention

    # You need to be connected, and you need to have access
    # as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id=self.object.company.id)

        if self.request.user.profile.isCentech():
            return super(SubventionDelete, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(SubventionDelete, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(SubventionDelete, self).get_context_data(**kwargs)
        context['companyId'] = kwargs['object'].company.id
        context['subvention'] = kwargs['object']
        return context

    # rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy(
            'finance:detail_finance',
            args={company_id}
        ))


class InvestissementCreate(generic.CreateView):
    # For create a new Investment
    model = Investissement
    template_name = 'finance/finance_form.html'
    form_class = InvestissementForm

    # You need to be connected, and you need to have access
    # as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        company = get_object_or_404(Company, id=self.args[0])

        if self.request.user.profile.isCentech():
            return super(InvestissementCreate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                    return super(InvestissementCreate, self).\
                        dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def form_valid(self, form):
        form.instance.company = Company.objects.get(id=int(self.args[0]))
        return super(InvestissementCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'finance:detail_finance',
            args={self.object.company.id}
        )


class InvestissementUpdate(generic.UpdateView):
    # For update an Investment
    model = Investissement
    form_class = InvestissementForm
    template_name = "finance/finance_form.html"

    # You need to be connected, and you need to have access
    # as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()

        if self.request.user.profile.isCentech():
            return super(InvestissementUpdate, self).\
                dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if self.request.user.profile.isFounder().company.all():
                return super(InvestissementUpdate, self).\
                    dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy(
            'finance:detail_finance',
            args={self.object.company.id}
        )


class InvestissementDelete(generic.DeleteView):
    # For delete an Investment
    model = Investissement

    # You need to be connected, and you need to have access
    # as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id=self.object.company.id)

        if self.request.user.profile.isCentech():
            return super(InvestissementDelete, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(InvestissementDelete, self).\
                    dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(InvestissementDelete, self).get_context_data(**kwargs)
        context['companyId'] = kwargs['object'].company.id
        context['subvention'] = kwargs['object']
        return context

    # rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy(
            'finance:detail_finance',
            args={company_id}
        ))


class PretCreate(generic.CreateView):
    # For create a new Loans
    model = Pret
    template_name = 'finance/finance_form.html'
    form_class = PretForm

    # You need to be connected, and you need to have access
    # as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        company = get_object_or_404(Company, id=self.args[0])

        if self.request.user.profile.isCentech():
            return super(PretCreate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(PretCreate, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def form_valid(self, form):
        form.instance.company = Company.objects.get(id=int(self.args[0]))
        return super(PretCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'finance:detail_finance',
            args={self.object.company.id}
        )


class PretUpdate(generic.UpdateView):
    # For update a Loans
    model = Pret
    form_class = PretForm
    template_name = "finance/finance_form.html"

    # You need to be connected, and you need to have access
    # as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(
            Company,
            id=self.object.company.id
        )

        if self.request.user.profile.isCentech():
            return super(PretUpdate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(PretUpdate, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy(
            'finance:detail_finance',
            args={self.object.company.id}
        )


class PretDelete(generic.DeleteView):
    # For delete a Loans
    model = Pret

    # You need to be connected, and you need to have access
    # as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id=self.object.company.id)

        if self.request.user.profile.isCentech():
            return super(PretDelete, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(PretDelete, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(PretDelete, self).get_context_data(**kwargs)
        context['companyId'] = kwargs['object'].company.id
        context['subvention'] = kwargs['object']
        return context

    # rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy(
            'finance:detail_finance',
            args={company_id}
        ))


class VenteCreate(generic.CreateView):
    # For create a new Sale
    model = Vente
    template_name = 'finance/finance_form.html'
    form_class = VenteForm

    # You need to be connected, and you need to have access
    # as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):

        company = get_object_or_404(Company, id=self.args[0])

        if self.request.user.profile.isCentech():
            return super(VenteCreate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(VenteCreate, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def form_valid(self, form):
        form.instance.company = Company.objects.get(id=int(self.args[0]))
        return super(VenteCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'finance:detail_finance',
            args={self.object.company.id}
        )


class VenteUpdate(generic.UpdateView):
    # For update a Sale
    model = Vente
    form_class = VenteForm
    template_name = "finance/finance_form.html"

    # You need to be connected, and you need to have access
    # as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(
            Company,
            id=self.object.company.id
        )

        if self.request.user.profile.isCentech():
            return super(VenteUpdate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(VenteUpdate, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_success_url(self, *args):
        self.object = self.get_object()
        return reverse_lazy(
            'finance:detail_finance',
            args={self.object.company.id}
        )


class VenteDelete(generic.DeleteView):
    # For delete a Sale
    model = Vente

    # You need to be connected, and you need to have access
    # as founder or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(
            Company,
            id=self.object.company.id
        )

        if self.request.user.profile.isCentech():
            return super(VenteDelete, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if self.request.user.profile.isFounder().company.all():
                return super(VenteDelete, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(VenteDelete, self).get_context_data(**kwargs)
        context['companyId'] = kwargs['object'].company.id
        context['subvention'] = kwargs['object']
        return context

    # rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy(
            'finance:detail_finance',
            args={company_id}
        ))
