# coding: utf-8

from django.shortcuts import render, render_to_response, get_object_or_404
from django.views import generic

from app.founder.models import Founder
from app.home.models import Expertise, Education
from app.company.models import Company

from app.founder.forms import FounderFilter, FounderForm
from app.home.forms import UserForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
import random
import os


class FounderCreate(generic.CreateView):
    model = User
    template_name = 'founder/founder_form.html'
    form_class = UserForm

    # You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # For know if the user is in the group "Centech"
        if self.request.user.profile.isCentech():
            return super(FounderCreate, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_success_url(self):
        # Create the founder associated
        founder = Founder.objects.create(user=self.object)

        # Defined the new password
        caractere = "abcdefghijklmnopqrstuvwxyz" \
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                    "0123456789"

        password = ""
        for index in range(10):
            password += random.choice(caractere)

        founder.user.set_password(password)
        founder.user.save()

        # Send welcome email
        self.send_courriel(founder, password)

        return reverse_lazy(
            "founder:detail",
            kwargs={
                'pk': founder.userProfile_id
            }
        )

    def send_courriel(self, founder, password):
        app = settings.DASHBOARD_APP

        message = u"Un compte vient de vous être créé pour accéder " \
                  u"au Tableau de Bord du Centech. Vous pouvez dès " \
                  u"maintenant vous y connecter avec les identifiants " \
                  u"ci-dessous : \n\n"

        message += u"Username : "
        message += founder.user.username
        message += u"\n"
        message += u"Password : "
        message += password
        message += u"\n"
        message += u"Lien : "
        message += app['site']['dns']
        message += u"\n\n\n"

        message += u"Pour toute question ou demande d'aide, " \
                   u"n'hésitais pas à nous contacter à l'adresse " \
                   u"suivante : "

        message += app['site']['email_technique']
        message += u"\n\n"
        message += u"Nous vous souhaitons une agréable journée!"
        message += u"\n\n"
        message += u"----------------------------------------\n\n"

        message += u"Ce message du Centech est un élément important " \
                   u"d'un programme auquel vous ou votre entreprise " \
                   u"participer. Si ce n'est pas le cas veuillez nous " \
                   u"en excuser et effacer ce message.\n"

        message += u"Si nous persistons à vous envoyer des courriel " \
                   u"sans votre accord, contacter nous à l'adresse " \
                   u"suivante : "
        message += app['site']['email_technique']

        emailReady = EmailMessage(
            'Bienvenue sur le Tableau de Bord du Centech',
            message,
            app['site']['email_technique'],
            [founder.user.email],
            [app['site']['email_technique']],
            reply_to=[app['site']['email_technique']]
        )

        emailReady.send(fail_silently=False)


class FounderUpdate(generic.UpdateView):
    # Update form
    model = Founder
    form_class = FounderForm
    template_name = "founder/founder_form.html"

    # You need to be connected, and you need to have access
    # as founder or centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.profile.isFounder():
            try:
                if int(self.request.user.profile.userProfile_id) \
                        == int(self.kwargs['pk']):
                    return super(FounderUpdate, self).dispatch(*args, **kwargs)
            except:
                pass

        if self.request.user.profile.isCentech():
            return super(FounderUpdate, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_success_url(self):
        return reverse_lazy("founder:detail", kwargs={'pk': self.kwargs['pk']})


class FounderIndex(generic.ListView):
    # List of founders
    model = Founder
    template_name = 'founder/index.html'
    context_object_name = 'founder_list'
    page_kwarg = 'page'
    paginate_by = 9

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.profile.isCentech():
            return super(FounderIndex, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            return super(FounderIndex, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isMentor():
            return super(FounderIndex, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isExecutive():
            return super(FounderIndex, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

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


class FounderView(generic.DetailView):
    # Display the detail of a founder
    model = Founder
    template_name = 'founder/detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.profile.isCentech():
            return super(FounderView, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            return super(FounderView, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isMentor():
            return super(FounderView, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isExecutive():
            return super(FounderView, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        founder = Founder.objects.get(userProfile_id=self.kwargs['pk'])
        companies = founder.company.all
        context = super(FounderView, self).get_context_data(**kwargs)
        context['companies'] = companies
        return context
