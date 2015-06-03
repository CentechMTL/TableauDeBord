# coding: utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import JsonResponse
from django.views import generic
from app.mentor.models import Mentor
from app.home.models import Education, Expertise
from app.mentor.forms import MentorFilter, MentorUpdateForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse

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
        form = self.form_class(object, request.POST)

        if form.is_valid():
            self.update_user(object, form)
            return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def update_user(self, object, form):
        object.user.last_name = form.data['lastname']
        object.user.first_name = form.data['firstname']

        object.phone = form.data['phone']
        object.website = form.data['website']
        object.about = form.data['about']

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

