# coding: utf-8

from django.http import HttpResponse, HttpResponseRedirect
from app.home.forms import UpdatePasswordForm,UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
import json
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from app.company.models import Company
from app.founder.models import Founder
from app.mentor.models import Mentor
from app.kpi.models import KPI, KpiType
from app.finance.models import Bourse, Subvention, Pret, Investissement, Vente
from django.db.models import Avg

#General view
class Summary(generic.TemplateView):
    template_name = 'home/summary.html'

    #You need to be connected, and you need to have access as centech only
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return super(Summary, self).dispatch(*args, **kwargs)

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        companies = Company.objects.all().order_by('incubated_on')
        founders = Founder.objects.all()
        mentors = Mentor.objects.all()

        grants = []
        for company in companies:
            totalGrants = 0
            for grant in company.grants.all():
                if grant.sommeReception:
                    totalGrants += grant.sommeReception
            grants.append((company, totalGrants))

        subsidies = []
        for company in companies:
            totalSubsidies = 0
            for subsidy in company.subsidies.all():
                if subsidy.sommeReception:
                    totalSubsidies += subsidy.sommeReception
            subsidies.append((company, totalSubsidies))

        investments = []
        for company in companies:
            totalInvestments = 0
            for investment in company.investments.all():
                if investment.sommeReception:
                    totalInvestments += investment.sommeReception
            investments.append((company, totalInvestments))

        sales = []
        for company in companies:
            totalSales = 0
            for sale in company.sales.all():
                if sale.sommeReception:
                    totalSales += sale.sommeReception
            sales.append((company, totalSales))

        loans = []
        for company in companies:
            totalLoans = 0
            for loan in company.loans.all():
                if loan.sommeReception:
                    totalLoans += loan.sommeReception
            loans.append((company, totalLoans))


        finances = {}
        finances['grants'] = grants
        finances['subsidies'] = subsidies
        finances['investments'] = investments
        finances['sales'] = sales
        finances['loans'] = loans

        context = super(Summary, self).get_context_data(**kwargs)
        context['companies'] = companies
        context['founders'] = founders
        context['mentors'] = mentors
        context['finances'] = finances
        return context

#Form for update password
class PasswordUpdate(generic.UpdateView):
    form_class = UpdatePasswordForm
    template_name = "home/password_update_form.html"
    model = User

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.user, request.POST)

        if form.is_valid():
            user = authenticate(username=request.user.username, password=form.data['password_old'])
            if(user == request.user):
                self.update_user(request.user, form)
                return self.form_valid(form)

        return render(request, self.template_name, {'form': form})

    def get_form(self, form_class):
        return form_class(self.request.user)

    def update_user(self, object, form):
        object.set_password(form.data['password_new'])

    def get_success_url(self):
        return reverse_lazy("company:index")

#Home page
def index(request):
    return render(request, 'home/index.html')

#NoAccessPermissions page
def noAccessPermissions(request):
    return render(request, 'home/noAccessPermissions.html')

#Set the session variable for the dashboard template
def setCompanyInSession(request, company_id):
    message= {}

    if request.is_ajax():
        request.session['companySelected'] = int(company_id)
        message['create'] = "True"

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')

    #The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")


#Register
#http://www.tangowithdjango.com/book17/chapters/login.html
def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'user/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")
