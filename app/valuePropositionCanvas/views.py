# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from app.company.models import Company
from app.founder.models import Founder
from app.mentor.models import Mentor
from app.valuePropositionCanvas.models import ValuePropositionCanvasElement, VALUE_PROPOSITION_CANVAS_TYPE_CHOICES
from app.businessCanvas.models import BusinessCanvasElement
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class ValuePropositionCanvasElementList(generic.ListView):
    model = ValuePropositionCanvasElement

    #You need to be connected, and you need to have access as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    idCompany = BusinessCanvasElement.objects.get(id=int(self.args[0])).company.id
                    company = Company.objects.get(id = idCompany) #If the company exist, else we go to except
                    return super(ValuePropositionCanvasElementList, self).dispatch(*args, **kwargs)
                except:
                    pass

        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(BusinessCanvasElement.objects.get(id=int(self.args[0])).company == int(company.id)):
                    return super(ValuePropositionCanvasElementList, self).dispatch(*args, **kwargs)
            except:
                pass

        #For know the company of the user if is a mentor
        if self.request.user.is_active:
            try:
                mentor = Mentor.objects.filter(user = self.request.user.id)
                company = Company.objects.get(mentors = mentor)
                if(int(self.args[0]) == int(company.id)):
                    return super(ValuePropositionCanvasElementList, self).dispatch(*args, **kwargs)
            except:
                pass

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(ValuePropositionCanvasElementList, self).get_context_data(**kwargs)
        context['valueProposition'] = self.args[0]
        context['title'] = BusinessCanvasElement.objects.get(id = self.args[0]).title

        valueProposition = self.args[0]

        listGains = ValuePropositionCanvasElement.objects.filter(type = VALUE_PROPOSITION_CANVAS_TYPE_CHOICES[0][0], valueProposition = valueProposition)
        context['listGains'] = listGains

        listPains = ValuePropositionCanvasElement.objects.filter(type = VALUE_PROPOSITION_CANVAS_TYPE_CHOICES[1][0], valueProposition = valueProposition)
        context['listPains'] = listPains

        listCustomerJobs = ValuePropositionCanvasElement.objects.filter(type = VALUE_PROPOSITION_CANVAS_TYPE_CHOICES[2][0], valueProposition = valueProposition)
        context['listCustomerJobs'] = listCustomerJobs

        listGainCreators = ValuePropositionCanvasElement.objects.filter(type = VALUE_PROPOSITION_CANVAS_TYPE_CHOICES[3][0], valueProposition = valueProposition)
        context['listGainCreators'] = listGainCreators

        listPainRelievers = ValuePropositionCanvasElement.objects.filter(type = VALUE_PROPOSITION_CANVAS_TYPE_CHOICES[4][0], valueProposition = valueProposition)
        context['listPainRelievers'] = listPainRelievers

        listProductAndServices = ValuePropositionCanvasElement.objects.filter(type = VALUE_PROPOSITION_CANVAS_TYPE_CHOICES[5][0], valueProposition = valueProposition)
        context['listProductAndServices'] = listProductAndServices

        return context

def deleteElement(request, element_id):
    message= {}

    if request.is_ajax():
        element = ValuePropositionCanvasElement.objects.get(id=element_id)
        element.delete()
        message['delete'] = "Deleted"

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')
    #The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")

def getDetail(request, element_id):
    message = {}

    if request.is_ajax():
        try:
            element = ValuePropositionCanvasElement.objects.get(id=element_id)
            message['title'] = element.title
            message['comment'] = element.comment
            message['type'] = element.type
        except:
            null

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')
    #The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")

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

            valueProposition = request.POST.get('valueProposition', '')
            try:
                valueProposition = BusinessCanvasElement.objects.get(id=valueProposition)
            except:
                error = True

            if error == False:
                if(request.POST.get('update', '') == "False"):
                    print typeName
                    element = ValuePropositionCanvasElement(title = title, comment = comment, type = typeName, valueProposition = valueProposition)
                    print element.title
                    print element.type
                    element.save()
                    id = element.id
                    return JsonResponse({'type': typeName, 'id': id, 'title': title, 'updated': 'False'})
                else:
                    id = request.POST.get('update', '')
                    element = ValuePropositionCanvasElement.objects.get(id = id)
                    element.title = title
                    element.comment = comment
                    element.save()
                    return JsonResponse({'type': typeName, 'id': id, 'title': title, 'updated': 'True'})
        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")
    #The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")