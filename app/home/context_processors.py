# coding: utf-8

from app.company.models import Company
from app.founder.models import Founder
from app.mentor.models import Mentor
from django.conf import settings

"""
    A context processor with all APP settings.
"""
def app_settings(request):
    return {'app': settings.DASHBOARD_APP}

#Make a list of company to insert in the main menu
def company_select(request):
    #For the list of company
    list_company = Company.objects.all().order_by('name')

    #For know if the user is in the group "Centech"
    isCentech = False
    groups = request.user.groups.values()
    for group in groups:
        if group['name'] == 'Centech':
            isCentech = True

    #For know if the user is a mentor
    isMentor = False
    if request.user.is_active:
        try:
            mentor = Mentor.objects.get(user = request.user.id)
            isMentor = True
        except:
            pass

    #For know if the user is a founder
    isFounder = False
    if request.user.is_active:
        try:
            founder = Founder.objects.get(user = request.user.id)
            isFounder = True
        except:
            pass

    #For know the list of company of the user if is a mentor
    listCompanyMentor = ""
    if request.user.is_active:
        try:
            mentor = Mentor.objects.get(user = request.user.id)
            listCompanyMentor = Company.objects.filter(mentors = mentor).order_by('name')
        except:
            pass

    #For know the company of the user if is a founder
    companyId = 0
    if request.user.is_active:
        try:
            founder = Founder.objects.get(user = request.user.id)
            company = Company.objects.get(founders = founder)
            companyId = company.id
        except:
            companyId = 0

    return {"isCentech": isCentech, "isMentor": isMentor, "isFounder": isFounder, "userCompanyId": companyId, "list_company_mentor": listCompanyMentor, "list_company": list_company}