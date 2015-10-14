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


class MentorCreate(generic.CreateView):
    model = User
    template_name = 'mentor/mentor_form.html'
    form_class = UserForm

    # You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.profile.isCentech():
            return super(MentorCreate, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_success_url(self):
        mentor = Mentor.objects.create(user=self.object)
        return reverse_lazy("mentor:detail", kwargs={'pk': mentor.userProfile_id})


# Form for update profile of a mentor
class MentorUpdate(generic.UpdateView):
    model = Mentor
    form_class = MentorForm

    # You need to be connected, and you need to have access as founder or centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # For know the company of the user if is a founder
        if self.request.user.profile.isMentor():
            try:
                if int(self.request.user.profile.userProfile_id) == int(self.kwargs['pk']):
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
        mentor = Mentor.objects.get(userProfile_id = self.kwargs['pk'])
        companies = Company.objects.filter(mentors = mentor)
        context = super(MentorView, self).get_context_data(**kwargs)
        context['companies'] = companies
        return context
