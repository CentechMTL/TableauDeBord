# coding: utf-8

from app.company.models import Company
from app.founder.models import Founder
from app.mentor.models import Mentor
from django.conf import settings
from app.home.views import setCompanyInSession

"""
    A context processor with all APP settings.
"""
def app_settings(request):
    return {'app': settings.DASHBOARD_APP}

#Make a list of company to insert in the main menu
def company_select(request):
    if request.user.is_active:
        #For know if the user is in the group "Centech"
        isCentech = request.user.profile.isCentech()

        #For know if the user is in the group "Centech"
        isExecutive = request.user.profile.isExecutive()

        #For know if the user is a mentor
        isMentor = request.user.profile.isMentor()

        #For know if the user is a founder
        isFounder = request.user.profile.isFounder()

        #For the list of company and menu
        list_company = []
        list_menu = []
        if isCentech:
            list_company = Company.objects.all().order_by('name')
            list_menu = ['companies', 'floor_plan', 'mentors', 'founders', 'road_map', 'summary', 'presence']
        else:
            if isMentor:
                list_company += isMentor.company.all()
                list_menu += ['companies', 'floor_plan', 'mentors', 'founders', 'road_map']
            if isFounder:
                list_company += isFounder.company.all()
                list_menu += ['companies', 'floor_plan', 'mentors', 'founders', 'road_map']
            if isExecutive:
                list_menu = ['companies', 'summary']

        #To set the default company selected
        if not list_company :
            setCompanyInSession(request, list_company[0].id)

    else:
        isCentech = False
        isExecutive = False
        isFounder = False
        isMentor = False
        list_company = ""
        list_menu = ""

    return {"isCentech": isCentech, "isExecutive": isExecutive, "isMentor": isMentor, "isFounder": isFounder, "list_company": list_company, "list_menu": list_menu}