from django.shortcuts import render, render_to_response, get_object_or_404
from django.views import generic
from app.founder.models import Founder
from app.home.models import Expertise, Education
from app.founder.forms import FounderFilter, FounderUpdateForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy, reverse

#Update form
class FounderUpdate(generic.UpdateView):
    model = Founder
    form_class = FounderUpdateForm
    template_name = "founder/founder_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FounderUpdate, self).dispatch(*args, **kwargs)

    def get_form(self, form_class):
        founder = self.get_object()
        form = form_class(founder)

        return form

    def get_object(self, queryset=None):
        return get_object_or_404(Founder, user=self.request.user)

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

        try:
            object.education = Education.objects.get(id = form.data['education'])
        except:
            pass

        object.expertise.clear()
        for expertise in form.cleaned_data["expertise"]:
                object.expertise.add(expertise)


    def get_success_url(self):
        return reverse_lazy("founder:detail", kwargs={'pk': int(self.request.user.profile.userProfile_id)})

#List of founders
class FounderIndex(generic.ListView):
    template_name = 'founder/index.html'
    context_object_name = 'founder'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FounderIndex, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        obj = Founder.objects.all()
        return obj

    def get_context_data(self, **kwargs):
        ff = FounderFilter(self.request.GET, queryset=Founder.objects.all())
        context = super(FounderIndex, self).get_context_data(**kwargs)
        context['filter'] = ff
        return context

#Display the detail of a founder
class FounderView(generic.DetailView):
    model = Founder
    template_name = 'founder/detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FounderView, self).dispatch(*args, **kwargs)