# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from app.businessCanvas.models import BusinessCanvasElement
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from app.company.models import Company
from app.founder.models import Founder
from app.mentor.models import Mentor
from app.businessCanvas.models import BusinessCanvasElement, Archive, BUSINESS_CANVAS_TYPE_CHOICES
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

#Archive the current business canvas of the company
def archiver(request, company_id):
    message= {}

    if request.is_ajax():
        company = Company.objects.get(id = company_id)
        elements = BusinessCanvasElement.objects.filter(company = company)
        archive = Archive(company = company)
        archive.save()
        for element in elements:
            if(element.disactivated == False):
                newElement = BusinessCanvasElement.objects.create(title = element.title, comment = element.comment, date = element.date, type = element.type, company = element.company, disactivated = True)
                newElement.save()
                archive.elements.add(newElement)
        message['date'] = str(archive.date)
        message['id'] = archive.id
        message['create'] = "True"

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')
    #The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")

#Delete an element of the business canvas
def deleteElement(request, element_id):
    message= {}

    if request.is_ajax():
        element = BusinessCanvasElement.objects.get(id=element_id)
        element.delete()
        message['delete'] = "Deleted"

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')
    #The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")

#Delete an archive
class ArchiveDelete(generic.DeleteView):
    model = Archive
    template_name = 'businessCanvas/archive_confirm_delete.html'

    #You need to be connected, and you need to have access as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know the company of the user if is a founder
        archive = Archive.objects.get(id=self.kwargs['pk'])
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(int(archive.company.id) == int(company.id)):
                    return super(ArchiveDelete, self).dispatch(*args, **kwargs)
            except:
                pass

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(ArchiveDelete, self).get_context_data(**kwargs)
        context['companyId'] = kwargs['object'].company.id
        context['archive'] = kwargs['object']
        return context

    #rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy('businessCanvas:businessCanvasElement_list', args = {company_id}))


#Delete an archive
def deleteArchive(request, archive_id):
    message= {}

    if request.is_ajax():
        archive = Archive.objects.get(id=archive_id)
        elements = archive.elements.filter()
        for element in elements:
            element.delete()
        archive.delete()
        message['delete'] = "Deleted"

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')
    #The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")


#Return detail of an element
def getDetail(request, element_id):
    message = {}

    if request.is_ajax():
        try:
            element = BusinessCanvasElement.objects.get(id=element_id)
            message['title'] = element.title
            message['comment'] = element.comment
            message['type'] = element.type
        except:
            pass

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')
    #The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")

#Add an element
def addElement(request):
    if request.is_ajax():
        if request.method == "POST":
            error = False
            title = request.POST.get('title', '')
            if title == None or title == "":
                error = True

            comment = request.POST.get('comment', '')
            if comment == None:
                comment = True

            typeName = request.POST.get('type', '')
            if typeName == None:
                error = True

            companyId = request.POST.get('company', '')
            if companyId == None:
                error = True

            if error == False:
                if(request.POST.get('update', '') == "False"):
                    type = typeName
                    company = Company.objects.get(id = companyId)
                    element = BusinessCanvasElement(title = title, comment = comment, type = type, company= company)
                    element.save()
                    id = element.id
                    return JsonResponse({'type': typeName, 'id': id, 'title': title, 'updated': 'False'})
                else:
                    id = request.POST.get('update', '')
                    element = BusinessCanvasElement.objects.get(id = id)
                    element.title = title
                    element.comment = comment
                    element.save()
                    return JsonResponse({'type': typeName, 'id': id, 'title': title, 'updated': 'True'})
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")
    #The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")

#Default page, display the current business canvas
class BusinessCanvasElementList(generic.ListView):
    model = BusinessCanvasElement

    #You need to be connected, and you need to have access as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    company = Company.objects.get(id = int(self.args[0])) #If the company exist, else we go to except
                    return super(BusinessCanvasElementList, self).dispatch(*args, **kwargs)
                except:
                    pass

        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(int(self.args[0]) == int(company.id)):
                    return super(BusinessCanvasElementList, self).dispatch(*args, **kwargs)
            except:
                pass

        #For know the company of the user if is a mentor
        if self.request.user.is_active:
            try:
                mentor = Mentor.objects.filter(user = self.request.user.id)
                company = Company.objects.get(mentors = mentor)
                if(int(self.args[0]) == int(company.id)):
                    return super(BusinessCanvasElementList, self).dispatch(*args, **kwargs)
            except:
                pass

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(BusinessCanvasElementList, self).get_context_data(**kwargs)
        isFounder = False
        listFounder = Founder.objects.filter(company__pk = self.args[0])
        for founder in listFounder:
            if founder.user.id == self.request.user.id:
                isFounder = True


        context['companyId'] = self.args[0]
        context['isFounder'] = isFounder

        company = Company.objects.get(id = self.args[0])
        archives = Archive.objects.filter(company = company).order_by('date')
        context['archives'] = archives

        for archive in archives:
            context['last_archive'] = archive

        keyPartner = BUSINESS_CANVAS_TYPE_CHOICES[0][0]
        listKeyPartners = BusinessCanvasElement.objects.filter(type = keyPartner, disactivated=False, company = company)
        context['listKeyPartners'] = listKeyPartners

        keyActivitie = BUSINESS_CANVAS_TYPE_CHOICES[1][0]
        listKeyActivities = BusinessCanvasElement.objects.filter(type = keyActivitie, disactivated=False, company = company)
        context['listKeyActivities'] = listKeyActivities

        valueProposition = BUSINESS_CANVAS_TYPE_CHOICES[2][0]
        listValuePropositions = BusinessCanvasElement.objects.filter(type = valueProposition, disactivated=False, company = company)
        context['listValuePropositions'] = listValuePropositions

        customerRelationship = BUSINESS_CANVAS_TYPE_CHOICES[3][0]
        listCustomerRelationships = BusinessCanvasElement.objects.filter(type = customerRelationship, disactivated=False, company = company)
        context['listCustomerRelationships'] = listCustomerRelationships

        keyResource = BUSINESS_CANVAS_TYPE_CHOICES[4][0]
        listKeyResources = BusinessCanvasElement.objects.filter(type = keyResource, disactivated=False, company = company)
        context['listKeyResources'] = listKeyResources

        channel = BUSINESS_CANVAS_TYPE_CHOICES[5][0]
        listChannels = BusinessCanvasElement.objects.filter(type = channel, disactivated=False, company = company)
        context['listChannels'] = listChannels

        customerSegment = BUSINESS_CANVAS_TYPE_CHOICES[6][0]
        listCustomerSegments = BusinessCanvasElement.objects.filter(type = customerSegment, disactivated=False, company = company)
        context['listCustomerSegments'] = listCustomerSegments

        costStructure = BUSINESS_CANVAS_TYPE_CHOICES[7][0]
        listCostStructures = BusinessCanvasElement.objects.filter(type = costStructure, disactivated=False, company = company)
        context['listCostStructures'] = listCostStructures

        revenueStream = BUSINESS_CANVAS_TYPE_CHOICES[8][0]
        listRevenueStreams = BusinessCanvasElement.objects.filter(type = revenueStream, disactivated=False, company = company)
        context['listRevenueStreams'] = listRevenueStreams

        brainstormingSpace = BUSINESS_CANVAS_TYPE_CHOICES[9][0]
        listBrainstormingSpaces = BusinessCanvasElement.objects.filter(type = brainstormingSpace, disactivated=False, company = company)
        context['listBrainstormingSpaces'] = listBrainstormingSpaces

        return context

#Display this archive in a table
class BusinessCanvasElementArchivedList(generic.ListView):
    model = BusinessCanvasElement
    template_name = "businessCanvas/businesscanvaselementarchived_list.html"

    #You need to be connected, and you need to have access as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                return super(BusinessCanvasElementArchivedList, self).dispatch(*args, **kwargs)

        #For know the company of the user if is a founder
        archive = Archive.objects.get(id=self.args[0])
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(int(archive.company.id) == int(company.id)):
                    return super(BusinessCanvasElementArchivedList, self).dispatch(*args, **kwargs)
            except:
                pass

        #For know the company of the user if is a mentor
        if self.request.user.is_active:
            try:
                mentor = Mentor.objects.filter(user = self.request.user.id)
                company = Company.objects.get(mentors = mentor)
                if(int(self.args[0]) == int(company.id)):
                    return super(BusinessCanvasElementArchivedList, self).dispatch(*args, **kwargs)
            except:
                pass

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(BusinessCanvasElementArchivedList, self).get_context_data(**kwargs)
        archive = Archive.objects.get(id = self.args[0])
        isFounder = False
        listFounder = Founder.objects.filter(company__pk = archive.company.id)
        for founder in listFounder:
            if founder.user.id == self.request.user.id:
                isFounder = True
        context['companyId'] = archive.company.id
        context['isFounder'] = isFounder

        context['currentArchive'] = archive

        company = archive.company
        archives = Archive.objects.filter(company = company)
        context['archives'] = archives

        keyPartner = BUSINESS_CANVAS_TYPE_CHOICES[0][0]
        listKeyPartners = archive.elements.filter(type = keyPartner, company = company)
        context['listKeyPartners'] = listKeyPartners

        keyActivitie = BUSINESS_CANVAS_TYPE_CHOICES[1][0]
        listKeyActivities = archive.elements.filter(type = keyActivitie, company = company)
        context['listKeyActivities'] = listKeyActivities

        valueProposition = BUSINESS_CANVAS_TYPE_CHOICES[2][0]
        listValuePropositions = archive.elements.filter(type = valueProposition, company = company)
        context['listValuePropositions'] = listValuePropositions

        customerRelationship = BUSINESS_CANVAS_TYPE_CHOICES[3][0]
        listCustomerRelationships = archive.elements.filter(type = customerRelationship, company = company)
        context['listCustomerRelationships'] = listCustomerRelationships

        keyResource = BUSINESS_CANVAS_TYPE_CHOICES[4][0]
        listKeyResources = archive.elements.filter(type = keyResource, company = company)
        context['listKeyResources'] = listKeyResources

        channel = BUSINESS_CANVAS_TYPE_CHOICES[5][0]
        listChannels = archive.elements.filter(type = channel, company = company)
        context['listChannels'] = listChannels

        customerSegment = BUSINESS_CANVAS_TYPE_CHOICES[6][0]
        listCustomerSegments = archive.elements.filter(type = customerSegment, company = company)
        context['listCustomerSegments'] = listCustomerSegments

        costStructure = BUSINESS_CANVAS_TYPE_CHOICES[7][0]
        listCostStructures = archive.elements.filter(type = costStructure, company = company)
        context['listCostStructures'] = listCostStructures

        revenueStream = BUSINESS_CANVAS_TYPE_CHOICES[8][0]
        listRevenueStreams = archive.elements.filter(type = revenueStream, company = company)
        context['listRevenueStreams'] = listRevenueStreams

        brainstormingSpace = BUSINESS_CANVAS_TYPE_CHOICES[9][0]
        listBrainstormingSpaces = archive.elements.filter(type = brainstormingSpace, company = company)
        context['listBrainstormingSpaces'] = listBrainstormingSpaces

        return context