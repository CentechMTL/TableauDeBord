# coding: utf-8

from django.shortcuts import render, render_to_response, get_object_or_404
from django.views import generic

from django.contrib.auth.models import User
from app.founder.models import Founder
from app.home.models import Expertise, Education
from app.company.models import Company

from app.founder.forms import FounderFilter, FounderUpdateForm, FounderCreateForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import random

class FounderCreate(generic.CreateView):
    model = Founder
    template_name = 'founder/founder_form.html'
    form_class = FounderCreateForm
    founderCreate = None

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return super(FounderCreate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self, form_class):
        form = form_class()

        return form

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            self.create_founder(form)
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def create_founder(self, form):
        lastname = form.data['lastname']
        firstname = form.data['firstname']
        username = form.data['username']
        email = form.data['email']
        newUser = User(username=username)

        caractere = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST0123456789"
        password = ""
        for index in range(10):
            password += random.choice(caractere)

        newUser.set_password(password)
        newUser.save()
        newUser.first_name = firstname
        newUser.last_name = lastname
        newUser.email = email
        newUser.save()

        newFounder = Founder(user = newUser)
        newFounder.save()
        self.founderCreate= newFounder
        newFounder.phone = form.data['phone']
        newFounder.website = form.data['website']

        newFounder.facebook = form.data['facebook']
        newFounder.twitter = form.data['twitter']
        newFounder.googlePlus = form.data['googlePlus']
        newFounder.linkedIn = form.data['linkedIn']

        newFounder.about = form.data['about']

        try:
            newFounder.picture = self.request.FILES['picture']
        except:
            pass

        try:
            newFounder.education = Education.objects.get(id = form.data['education'])
        except:
            pass

        for expertise in form.cleaned_data["expertise"]:
                newFounder.expertise.add(expertise)

        newFounder.save()

        app = settings.DASHBOARD_APP
        message = u"Un compte vient de vous être créé pour accéder au Tableau de Bord du Centech. Vous pouvez dès maintenant vous y connecter avec les identifiants ci-dessous : \n\n"
        message += u"Username : "
        message += username
        message += u"\n"
        message += u"Password : "
        message += password
        message += u"\n\n\n"
        message += u"Pour toute question ou demande d'aide, n'hésitais pas à nous contacter à l'adresse suivante : "
        message += app['site']['email_technique']
        message += u"\n\n"
        message += u"Nous vous souhaitons une agréable journée!"
        message += u"\n\n"
        message += u"----------------------------------------\n\n"
        message += u"Ce message du Centech est un élément important d'un programme auquel vous ou votre entreprise participer. Si ce n'est pas le cas veuillez nous en excuser et effacer ce message.\n"
        message += u"Si nous persistons à vous envoyer des courriel sans votre accord, contacter nous à l'adresse suivante : "
        message += app['site']['email_technique']

        send_mail('Bienvenue sur le Tableau de Bord du Centech', message, app['site']['email_technique'], [app['site']['email_technique'], email], fail_silently=False)

    def get_success_url(self):
        return reverse_lazy("founder:detail", kwargs={'pk': self.founderCreate.userProfile_id})


#Update form
class FounderUpdate(generic.UpdateView):
    model = Founder
    form_class = FounderUpdateForm
    template_name = "founder/founder_form.html"

    #You need to be connected, and you need to have access as founder or centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                if(int(self.request.user.profile.userProfile_id) == int(self.kwargs['pk'])):
                    return super(FounderUpdate, self).dispatch(*args, **kwargs)
            except:
                pass

        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return super(FounderUpdate, self).dispatch(*args, **kwargs)
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self, form_class):
        founder = self.get_object()
        form = form_class(founder)

        return form

    def get_object(self, queryset=None):
        return get_object_or_404(Founder, userProfile_id=self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        form = self.form_class(object, request.POST, request.FILES)

        if form.is_valid():
            self.update_user(object, form)
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def update_user(self, object, form):
        object.user.last_name = form.data['lastname']
        object.user.first_name = form.data['firstname']

        object.phone = form.data['phone']
        object.website = form.data['website']
        object.facebook = form.data['facebook']
        object.twitter = form.data['twitter']
        object.googlePlus = form.data['googlePlus']
        object.linkedIn = form.data['linkedIn']
        object.about = form.data['about']

        try:
            object.picture = self.request.FILES['picture']
        except:
            pass

        try:
            object.education = Education.objects.get(id = form.data['education'])
        except:
            pass

        object.expertise.clear()
        for expertise in form.cleaned_data["expertise"]:
                object.expertise.add(expertise)


    def get_success_url(self):
        return reverse_lazy("founder:detail", kwargs={'pk': self.kwargs['pk']})

#List of founders
class FounderIndex(generic.ListView):
    model = Founder
    template_name = 'founder/index.html'
    context_object_name = 'founder_list'
    page_kwarg = 'page'
    paginate_by = 9

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FounderIndex, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        ff = FounderFilter(self.request.GET)
        return ff.qs
    def get_context_data(self, **kwargs):
        ff = FounderFilter(self.request.GET, queryset=self.get_queryset())
        context = super(FounderIndex, self).get_context_data(**kwargs)
        context['filter'] = ff

        text = ""
        compteur = 0
        for getVariable in self.request.GET:
            for getValue in self.request.GET.getlist(getVariable):
                if compteur == 0:
                    text += "?" + getVariable + "=" + getValue
                else:
                    text += "&" + getVariable + "=" + getValue
                compteur += 1
        context['get'] = text

        return context

#Display the detail of a founder
class FounderView(generic.DetailView):
    model = Founder
    template_name = 'founder/detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FounderView, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        founder = Founder.objects.get(userProfile_id = self.kwargs['pk'])
        companies = founder.company.all
            #Company.objects.filter(founders = founder)
        context = super(FounderView, self).get_context_data(**kwargs)
        context['companies'] = companies
        return context
