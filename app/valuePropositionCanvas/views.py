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
from app.valuePropositionCanvas.models import \
    ValuePropositionCanvasElement, ValuePropositionCanvasType
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


class ValuePropositionCanvasElementList(generic.ListView):
    model = ValuePropositionCanvasElement

    # You need to be connected, and you need to have access
    # as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        # For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    # If the company exist, else we go to except
                    company = Company.objects.get(id=int(self.args[0]))
                    return super(ValuePropositionCanvasElementList, self).\
                        dispatch(*args, **kwargs)
                except:
                    pass

        # For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user=self.request.user.id)
                company = Company.objects.get(founders=founder)
                if int(self.args[0]) == int(company.id):
                    return super(ValuePropositionCanvasElementList, self).\
                        dispatch(*args, **kwargs)
            except:
                pass

        # For know the company of the user if is a mentor
        if self.request.user.is_active:
            try:
                mentor = Mentor.objects.filter(user=self.request.user.id)
                company = Company.objects.get(mentors=mentor)
                if int(self.args[0]) == int(company.id):
                    return super(ValuePropositionCanvasElementList, self).\
                        dispatch(*args, **kwargs)
            except:
                pass

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(ValuePropositionCanvasElementList, self).\
            get_context_data(**kwargs)
        isFounder = False
        listFounder = Founder.objects.filter(company__pk=self.args[0])
        for founder in listFounder:
            if founder.user.id == self.request.user.id:
                isFounder = True

        context['companyId'] = self.args[0]
        context['isFounder'] = isFounder

        company = Company.objects.get(id=self.args[0])

        Gain = ValuePropositionCanvasType.objects.get(name="Gain")
        listGains = ValuePropositionCanvasElement.objects.filter(
            type=Gain,
            company=company
        )
        context['listGains'] = listGains

        Pain = ValuePropositionCanvasType.objects.get(name="Pain")
        listPains = ValuePropositionCanvasElement.objects.filter(
            type=Pain,
            company=company
        )
        context['listPains'] = listPains

        customerJob = ValuePropositionCanvasType.objects.get(
            name="CustomerJob"
        )
        listCustomerJobs = ValuePropositionCanvasElement.objects.filter(
            type=customerJob,
            company=company
        )
        context['listCustomerJobs'] = listCustomerJobs

        gainCreator = ValuePropositionCanvasType.objects.get(
            name="GainCreator"
        )
        listGainCreators = ValuePropositionCanvasElement.objects.filter(
            type=gainCreator,
            company=company
        )
        context['listGainCreators'] = listGainCreators

        painReliever = ValuePropositionCanvasType.objects.get(
            name="PainReliever"
        )
        listPainRelievers = ValuePropositionCanvasElement.objects.filter(
            type=painReliever,
            company=company
        )
        context['listPainRelievers'] = listPainRelievers

        productAndService = ValuePropositionCanvasType.objects.get(
            name="ProductAndService"
        )
        listProductAndServices = ValuePropositionCanvasElement.objects.filter(
            type=productAndService,
            company=company
        )
        context['listProductAndServices'] = listProductAndServices

        return context


def deleteElement(request, element_id):
    message = {}

    if request.is_ajax():
        element = ValuePropositionCanvasElement.objects.get(id=element_id)
        element.delete()
        message['delete'] = "Deleted"

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')
    # The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")


def getDetail(request, element_id):
    message = {}

    if request.is_ajax():
        try:
            element = ValuePropositionCanvasElement.objects.get(id=element_id)
            message['title'] = element.title
            message['comment'] = element.comment
            message['type'] = element.type.name
        except:
            pass

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')
    # The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")


def addElement(request):
    if request.is_ajax():
        if request.method == "POST":
            error = False
            title = request.POST.get('title', '')
            if title is None or title == "":
                error = True

            comment = request.POST.get('comment', '')
            if comment is None:
                comment = True

            typeName = request.POST.get('type', '')
            if typeName is None:
                error = True

            companyId = request.POST.get('company', '')
            if companyId is None:
                error = True

            if not error:
                if request.POST.get('update', '') == "False":
                    type = ValuePropositionCanvasType.objects.get(
                        name=typeName
                    )
                    company = Company.objects.get(id=companyId)
                    element = ValuePropositionCanvasElement(
                        title=title,
                        comment=comment,
                        type=type,
                        company=company
                    )
                    element.save()
                    id = element.id
                    return JsonResponse(
                        {
                            'type': typeName,
                            'id': id,
                            'title': title,
                            'updated': 'False'
                        }
                    )
                else:
                    id = request.POST.get('update', '')
                    element = ValuePropositionCanvasElement.objects.get(id=id)
                    element.title = title
                    element.comment = comment
                    element.save()
                    return JsonResponse(
                        {
                            'type': typeName,
                            'id': id,
                            'title': title,
                            'updated': 'True'
                        }
                    )

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    # The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")
