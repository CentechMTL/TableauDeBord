# coding: utf-8

from django.http import HttpResponseRedirect
from django.views import generic

from django.contrib.auth.models import User
from app.mentor.models import Mentor
from app.company.models import Company

from app.mentor.forms import MentorFilter, MentorForm
from app.home.forms import UserForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

from django.conf import settings
import random
from django.core.mail import EmailMessage

import random


class MentorCreate(generic.CreateView):
    model = User
    template_name = 'mentor/mentor_form.html'
    form_class = UserForm

    # You need to be connected, and you need to have access
    # as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.profile.isCentech():
            return super(MentorCreate, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_success_url(self):
        # Create the mentor associated
        mentor = Mentor.objects.create(user=self.object)

        # Defined the new password
        caractere = "abcdefghijklmnopqrstuvwxyz" \
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                    "0123456789"

        password = ""

        for index in range(10):
            password += random.choice(caractere)

        mentor.user.set_password(password)
        mentor.user.save()

        # Send welcome email
        self.send_courriel(mentor, password)

        return reverse_lazy(
            "mentor:detail",
            kwargs={
                'pk': mentor.userProfile_id
            }
        )

    def send_courriel(self, mentor, password):
        app = settings.DASHBOARD_APP

        message = u"Un compte vient de vous être créé pour accéder " \
                  u"au Tableau de Bord du Centech. Vous pouvez dès " \
                  u"maintenant vous y connecter avec les identifiants " \
                  u"ci-dessous : \n\n"

        message += u"Username : "
        message += mentor.user.username
        message += u"\n"
        message += u"Password : "
        message += password
        message += u"\n"
        message += u"Lien : "
        message += app['site']['dns']
        message += u"\n\n\n"

        message += u"Pour toute question ou demande d'aide, n'hésitais " \
                   u"pas à nous contacter à l'adresse suivante : "

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
            [mentor.user.email],
            [app['site']['email_technique']],
            reply_to=[app['site']['email_technique']]
        )

        emailReady.send(fail_silently=False)


# Form for update profile of a mentor
class MentorUpdate(generic.UpdateView):
    model = Mentor
    form_class = MentorForm

    # You need to be connected, and you need to have access
    # as founder or centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # For know the company of the user if is a founder
        if self.request.user.profile.isMentor():
            try:
                if int(self.request.user.profile.userProfile_id) \
                        == int(self.kwargs['pk']):
                    return super(MentorUpdate, self).dispatch(*args, **kwargs)
            except:
                pass

        if self.request.user.profile.isCentech():
            return super(MentorUpdate, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_success_url(self):
        return reverse_lazy("mentor:detail", kwargs={'pk': self.kwargs['pk']})


class MentorIndex(generic.ListView):
    # List of all mentors
    template_name = 'mentor/index.html'
    context_object_name = 'mentors'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.profile.isCentech():
            return super(MentorIndex, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            return super(MentorIndex, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isMentor():
            return super(MentorIndex, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isExecutive():
            return super(MentorIndex, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_queryset(self):
        return Mentor.objects.all()

    def get_context_data(self, **kwargs):
        mf = MentorFilter(self.request.GET, queryset=Mentor.objects.all())
        context = super(MentorIndex, self).get_context_data(**kwargs)
        context['mentorFilter'] = mf
        return context


class MentorView(generic.DetailView):
    # Display detail of a mentor
    model = Mentor
    template_name = 'mentor/detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.profile.isCentech():
            return super(MentorView, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            return super(MentorView, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isMentor():
            return super(MentorView, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isExecutive():
            return super(MentorView, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        mentor = Mentor.objects.get(userProfile_id=self.kwargs['pk'])
        companies = Company.objects.filter(mentors=mentor)
        context = super(MentorView, self).get_context_data(**kwargs)
        context['companies'] = companies
        return context
