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
from django.db.models import Avg

from app.company.models import Company
from app.founder.models import Founder
from app.mentor.models import Mentor
from app.kpi.models import KPI, KPI_TYPE_CHOICES
from app.finance.models import Bourse, Subvention, Pret, Investissement, Vente
from app.experiment.models import CustomerExperiment

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
        finances['bourses'] = grants
        finances['subventions'] = subsidies
        finances['investissements'] = investments
        finances['ventes'] = sales
        finances['prêts'] = loans

        KPIs = []
        for company in companies:
            KPIs.append((company, company.get_last_irl(), company.get_last_trl()))

        experiments = []
        for company in companies:
            inProgress = company.experiments.filter(validated = None).count()
            validated = company.experiments.filter(validated = True).count()
            lastExperiment = company.get_last_experiment()
            experiments.append((company, inProgress, validated, lastExperiment))

        context = super(Summary, self).get_context_data(**kwargs)

        context['companies'] = companies
        context['founders'] = founders
        context['mentors'] = mentors
        context['finances'] = finances

        context['KPI'] = KPIs
        context['averageIRL'] = round(KPI.objects.filter(type=KPI_TYPE_CHOICES[0][0]).aggregate(Avg('level')).values()[0], 2)
        context['averageTRL'] = round(KPI.objects.filter(type=KPI_TYPE_CHOICES[1][0]).aggregate(Avg('level')).values()[0], 2)

        context['experiments'] = experiments
        context['experiments_inProgress_count'] = CustomerExperiment.objects.filter(validated = None).count()
        context['experiments_validated_count'] = CustomerExperiment.objects.filter(validated = True).count()

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

    auth = False

    try:
        #The user is admin
        groups = request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                auth = True

        #The user is mentor for this company
        mentor = Mentor.objects.get(user = request.user.id)
        print(request.user.id)
        companies = Company.objects.filter(mentors = mentor)
        for company in companies:
            if(int(company_id) == int(company.id)):
                auth = True
        else:
            pass
    except:
        auth = True

    if auth:
        request.session['companySelected'] = int(company_id)
        message['create'] = "True"

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")

from django.template import loader, Context
import os
from centech2 import settings

def generate_presentation(request):

    title = "Présentation générale du Centech"

    template_file = 'home/result.tex'

    t = loader.get_template(template_file)
    context = Context({
              "title":    title,
              })


    commande = "pandoc -t beamer " + os.path.join(settings.BASE_DIR, "app/home/templates/home/") + "result" + ".tex " + "-o " + os.path.join(settings.BASE_DIR, "media/generated_pandoc/") + "result" + ".pdf"
    print settings.BASE_DIR
    print commande
    os.system(commande)

    path_pdf = os.path.join(settings.BASE_DIR, "media/generated_pandoc/") + 'result.pdf'
    response = HttpResponse(
        open(path_pdf, 'rb').read(),
        content_type="application_pdf")
    response["Content-Disposition"] = \
        "attachment; filename=presentation_centech.pdf"

    return response
