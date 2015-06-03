# coding: utf-8

from django.shortcuts import render_to_response, get_object_or_404, render
from app.company.models import Company, Presence, CompanyStatus
from app.founder.models import Founder
from app.company.forms import CompanyFilter, CompanyUpdateForm, CompanyCreateForm, CompanyStatusCreateForm
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages


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
        return super(CompanyView, self).dispatch(*args, **kwargs)

class CompanyStatusCreate(generic.CreateView):
    model = CompanyStatus
    template_name = 'company/company_form.html'
    form_class = CompanyStatusCreateForm

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return super(CompanyStatusCreate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self, form_class):
        form = form_class()
        return form

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid(form):
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
        return (u'Ce nom existe déjà.')

    def get_success_message(self):
        return (u'Le status a bien été ajouté.')

class CompanyCreate(generic.CreateView):
    model = Company
    template_name = 'company/company_form.html'
    form_class = CompanyCreateForm

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
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
        description = form.data['about']

        newCompany = Company(name=name, companyStatus=status, video=video, url=url, description=description)
        newCompany.save()

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
    form_class = CompanyUpdateForm
    template_name = "company/company_form.html"

    #You need to be connected, and you need to have access as founder or centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(int(self.kwargs["pk"]) == int(company.id)):
                    return super(CompanyUpdate, self).dispatch(*args, **kwargs)
            except:
                pass

        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
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
        object.description = form.data['about']
        try:
            object.logo = self.request.FILES['logo']
        except:
            pass
        object.video = form.data['video']

    def get_success_url(self):
        return reverse_lazy("company:detail", kwargs={'pk': int(self.kwargs["pk"])})

#Display all presence
class PresenceList(generic.ListView):
    template_name = 'company/presence.html'
    context_object_name = 'presence'

   #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return super(PresenceList, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_queryset(self):
        return Presence.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PresenceList, self).get_context_data(**kwargs)
        #TODO Revoir le système d'affichage des présences
        emergence = CompanyStatus.objects.get(status = "Emergence Mai 2015")
        companies = Company.objects.filter(companyStatus = emergence)
        context['companies'] = companies
        presences = Presence.objects.all()
        context['presence_list'] = presences

        return context

#Add a new presence
class PresenceAdd(generic.CreateView):
    model = Presence
    fields = ['company','date']

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
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
        return reverse_lazy('company:presence_list')

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return super(PresenceUpdate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

#Delete the presence
class PresenceDelete(generic.DeleteView):
    model = Presence


    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return super(PresenceDelete, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_success_url(self, **kwargs):
        return reverse_lazy('company:presence_list')

    def get_context_data(self, **kwargs):
        context = super(PresenceDelete, self).get_context_data(**kwargs)
        context['presence'] = kwargs['object']
        return context