from django.shortcuts import render_to_response, get_object_or_404, render
from app.company.models import Company, Presence, CompanyStatus
from app.founder.models import Founder
from app.company.forms import CompanyFilter, CompanyUpdateForm
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

#Update form
class CompanyUpdate(generic.UpdateView):
    model = Company
    form_class = CompanyUpdateForm
    template_name = "company/company_form.html"

    #You need to be connected, and you need to have access as founder only
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
        object.logo = self.request.FILES['logo']
        object.video = form.data['video']

    def get_success_url(self):
        return reverse_lazy("company:detail", kwargs={'pk': int(self.kwargs["pk"])})


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
        cf = CompanyFilter(self.request.GET, queryset=Company.objects.all())
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

def filter(request):
    f = CompanyFilter(request.GET, queryset=Company.objects.all())
    return render_to_response('company/filter.html', {'filter': f})

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
        emergence = CompanyStatus.objects.filter(status = "Emergence")
        companies = Company.objects.filter(companyStatus = emergence[0])
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