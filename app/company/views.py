# coding: utf-8

from django.shortcuts import render_to_response, get_object_or_404, render
from app.company.models import Company, Presence, CompanyStatus
from app.founder.models import Founder
from app.company.forms import CompanyFilter, MiniCompanyUpdateForm, CompanyUpdateForm, CompanyCreateForm, CompanyStatusCreateForm
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
import os

from app.home.views import setCompanyInSession

def filter(request):
    f = CompanyFilter(request.GET, queryset=Company.objects.filter(name__icontains= request.GET['name']))
    return render_to_response('company/filter.html', {'filter': f})

#List all companies in the Centech
class CompanyIndex(generic.ListView):
    template_name = 'company/index.html'
    context_object_name = 'company'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CompanyIndex, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Company.objects.all()

    def get_context_data(self, **kwargs):
        cf = CompanyFilter(self.request.GET, queryset=Company.objects.order_by('name'))
        context = super(CompanyIndex, self).get_context_data(**kwargs)
        context['filter'] = cf


        return context

#Display detail of the company
class CompanyView(generic.DetailView):
    model = Company
    template_name = 'company/detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        setCompanyInSession(self.request, self.kwargs['pk'])
        return super(CompanyView, self).dispatch(*args, **kwargs)


class CompanyStatusCreate(generic.CreateView):
    model = CompanyStatus
    template_name = 'company/company_form.html'
    form_class = CompanyStatusCreateForm

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.profile.isCentech():
            return super(CompanyStatusCreate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self, form_class):
        form = form_class()
        return form

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            self.create_status(form)
            messages.success(self.request, self.get_success_message())
            return self.form_valid(form)
        else:
            messages.error(self.request, self.get_error_message())
            return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def create_status(self, form):
        name = form.data['name']
        newStatus = CompanyStatus(status=name)
        newStatus.save()

    def get_success_url(self):
        return reverse_lazy("company:index")

    def get_error_message(self):
        return (u'Ce nom existe déjà ou est invalide.')

    def get_success_message(self):
        return (u'Le status a bien été ajouté.')

class CompanyCreate(generic.CreateView):
    model = Company
    template_name = 'company/company_form.html'
    form_class = CompanyCreateForm

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.profile.isCentech():
            return super(CompanyCreate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self, form_class):
        form = form_class()

        return form

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            self.create_company(form)
            messages.success(self.request, self.get_success_message())
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def create_company(self, form):
        name = form.data['name']
        status = CompanyStatus.objects.get(id = form.data['status'])
        video = form.data['video']
        url = form.data['url']
        facebook = form.data['facebook']
        twitter = form.data['twitter']
        googlePlus = form.data['googlePlus']
        linkedIn = form.data['linkedIn']
        description = form.data['about']

        newCompany = Company(name=name,
                             companyStatus=status,
                             video=video,
                             url=url,
                             description=description,
                             facebook=facebook,
                             twitter=twitter,
                             googlePlus=googlePlus,
                             linkedIn=linkedIn)
        newCompany.save()

        try:
            if(form.data['incubated_on'] != ""):
                newCompany.incubated_on = form.data['incubated_on']
            if(form.data['endOfIncubation'] != ""):
                newCompany.endOfIncubation = form.data['endOfIncubation']
        except:
            pass

        try:
            newCompany.logo = self.request.FILES['logo']
        except:
            pass

        for founder in form.cleaned_data["founders"]:
                newCompany.founders.add(founder)

        for mentor in form.cleaned_data["mentors"]:
                newCompany.mentors.add(mentor)

        newCompany.save()

    def get_success_url(self):
        return reverse_lazy("company:index")

    def get_success_message(self):
        return (u'La compagnie a bien été ajouté.')

#Update form
class CompanyUpdate(generic.UpdateView):
    model = Company
    template_name = "company/company_form.html"

    #You need to be connected, and you need to have access as founder or centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        company = get_object_or_404(Company, id=self.kwargs["pk"])

        #Let the centech in first for allow modify a company of a founder who work in the Centech
        if self.request.user.profile.isCentech():
            self.form_class = CompanyUpdateForm
            return super(CompanyUpdate, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                self.form_class = MiniCompanyUpdateForm
                return super(CompanyUpdate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self, form_class):
        company = self.get_object()
        form = form_class(company)

        return form

    def get_object(self, queryset=None):
        return get_object_or_404(Company, id=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        form = self.form_class(object, request.POST, request.FILES)
        if form.is_valid():
            self.update_company(object, form)
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def update_company(self, object, form):
        object.name = form.data['name']
        object.url = form.data['url']
        object.facebook = form.data['facebook']
        object.twitter = form.data['twitter']
        object.googlePlus = form.data['googlePlus']
        object.linkedIn = form.data['linkedIn']
        object.description = form.data['about']
        object.video = form.data['video']

        try:
            self.request.FILES['logo'].name = object.name + os.path.splitext(self.request.FILES['logo'].name)[1]
            object.logo = self.request.FILES['logo']
        except:
            pass

        try:
            object.companyStatus = CompanyStatus.objects.get(id = form.data['status'])
        except:
            pass

        try:
            if form.data['incubated_on'] != "":
                object.incubated_on = form.data['incubated_on']
            else:
                object.incubated_on = None

            if form.data['endOfIncubation'] != "":
                object.endOfIncubation = form.data['endOfIncubation']
            else:
                object.endOfIncubation = None
        except:
            pass

        try:
            if form.data['founders']:
                object.founders.clear()
                for founder in form.cleaned_data["founders"]:
                        object.founders.add(founder)
        except:
            pass

        try:
            if form.data['mentors']:
                object.mentors.clear()
                for mentor in form.cleaned_data["mentors"]:
                        object.mentors.add(mentor)
        except:
            pass
    def get_success_url(self):
        return reverse_lazy("company:detail", kwargs={'pk': int(self.kwargs["pk"])})

#Display all presence
class PresenceList(generic.ListView):
    template_name = 'company/presence.html'
    context_object_name = 'presence'

   #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.profile.isCentech():
            return super(PresenceList, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_queryset(self):
        return Presence.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PresenceList, self).get_context_data(**kwargs)
        status = CompanyStatus.objects.get(id = self.kwargs['status'])
        companies = Company.objects.filter(companyStatus = status)
        context['companies'] = companies
        allPresences = Presence.objects.all()
        presences = []
        for presence in allPresences:
            for company in presence.company.all():
                if company.companyStatus == status:
                    print company.name
                    print presence
                    print len(presences)
                    presences.append(presence)
                    break

        context['presence_list'] = presences
        context['status_selected'] = status
        context['list_company_status'] = CompanyStatus.objects.all()

        return context

#Add a new presence
class PresenceAdd(generic.CreateView):
    model = Presence
    fields = ['company','date']

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.profile.isCentech():
            return super(PresenceAdd, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def form_valid(self, form):
         return super(PresenceAdd, self).form_valid(form)

#Update the presence
class PresenceUpdate(generic.UpdateView):
    model = Presence
    fields = ['company','date']

    def get_url(self):
        return reverse_lazy('company:presence_list', self.object.get_absolute_url())

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.profile.isCentech():
            return super(PresenceUpdate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

#Delete the presence
class PresenceDelete(generic.DeleteView):
    model = Presence


    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.profile.isCentech():
            return super(PresenceDelete, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_success_url(self, **kwargs):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        context = super(PresenceDelete, self).get_context_data(**kwargs)
        context['presence'] = kwargs['object']
        context['status'] = kwargs['object'].company.all()[0].companyStatus.id
        return context