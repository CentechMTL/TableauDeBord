# coding: utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import JsonResponse
from django.views import generic

from django.contrib.auth.models import User
from app.mentor.models import Mentor
from app.home.models import Education, Expertise
from app.company.models import Company

from app.mentor.forms import MentorFilter, MentorUpdateForm, MentorCreateForm

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import random
import os

class MentorCreate(generic.CreateView):
    model = Mentor
    template_name = 'mentor/mentor_form.html'
    form_class = MentorCreateForm
    mentorCreate = None

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return super(MentorCreate, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self, form_class):
        form = form_class()

        return form

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            self.create_mentor(form)
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def create_mentor(self, form):
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

        newMentor = Mentor(user = newUser)
        newMentor.save()
        self.mentorCreate= newMentor
        newMentor.phone = form.data['phone']
        newMentor.website = form.data['website']
        newMentor.facebook = form.data['facebook']
        newMentor.twitter = form.data['twitter']
        newMentor.googlePlus = form.data['googlePlus']
        newMentor.linkedIn = form.data['linkedIn']
        newMentor.about = form.data['about']
        newMentor.type = form.data['type']
        newMentor.url = form.data['url']

        try:
            newMentor.picture = self.request.FILES['picture']
        except:
            pass

        for expertise in form.cleaned_data["expertise"]:
                newMentor.expertise.add(expertise)

        newMentor.save()

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
        return reverse_lazy("mentor:detail", kwargs={'pk': self.mentorCreate.userProfile_id})

#Form for update profile of a mentor
class MentorUpdate(generic.UpdateView):
    model = Mentor
    form_class = MentorUpdateForm

    #You need to be connected, and you need to have access as founder or centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                if(int(self.request.user.profile.userProfile_id) == int(self.kwargs['pk'])):
                    return super(MentorUpdate, self).dispatch(*args, **kwargs)
            except:
                pass

        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return super(MentorUpdate, self).dispatch(*args, **kwargs)
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_form(self, form_class):
        mentor = self.get_object()
        form = form_class(mentor)

        return form

    def get_object(self, queryset=None):
        return get_object_or_404(Mentor, userProfile_id=self.kwargs['pk'])

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
        object.type = form.data['type']
        object.url = form.data['url']

        try:
            self.request.FILES['picture'].name = object.user.username + os.path.splitext(self.request.FILES['picture'].name)[1]
            object.picture = self.request.FILES['picture']
        except:
            pass

        object.expertise.clear()
        for expertise in form.cleaned_data["expertise"]:
                object.expertise.add(expertise)

    def get_success_url(self):
        return reverse_lazy("mentor:detail", kwargs={'pk': self.kwargs['pk']})

#List of all mentors
class MentorIndex(generic.ListView):
    template_name = 'mentor/index.html'
    context_object_name = 'mentors'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MentorIndex, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        obj = Mentor.objects.all()
        return Mentor.objects.all()

    def get_context_data(self, **kwargs):
        mf = MentorFilter(self.request.GET, queryset=Mentor.objects.all())
        context = super(MentorIndex, self).get_context_data(**kwargs)
        context['mentorFilter'] = mf
        return context

#Display detail of a mentor
class MentorView(generic.DetailView):
    model = Mentor
    template_name = 'mentor/detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MentorView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        mentor = Mentor.objects.get(userProfile_id = self.kwargs['pk'])
        companies = Company.objects.filter(mentors = mentor)
        context = super(MentorView, self).get_context_data(**kwargs)
        context['companies'] = companies
        return context
