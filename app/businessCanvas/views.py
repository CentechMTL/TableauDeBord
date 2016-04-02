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
from app.businessCanvas.models import BusinessCanvasElement, \
    Archive, BUSINESS_CANVAS_TYPE_CHOICES
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Archive the current business canvas of the company
def archiver(request, company_id):
    message = {}

    if request.is_ajax():
        company = Company.objects.get(id=company_id)
        elements = BusinessCanvasElement.objects.filter(company=company)
        archive = Archive(company=company)
        archive.save()
        for element in elements:
            if element.disactivated is False:
                new_element = BusinessCanvasElement.objects.create(
                    title=element.title,
                    comment=element.comment,
                    date=element.date,
                    type=element.type,
                    company=element.company,
                    disactivated=True
                )

                new_element.save()
                archive.elements.add(new_element)
        message['date'] = str(archive.date)
        message['id'] = archive.id
        message['create'] = "True"

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')
    # The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")


# Delete an element of the business canvas
def deleteElement(request, element_id):
    message = {}

    if request.is_ajax():
        element = BusinessCanvasElement.objects.get(id=element_id)
        element.delete()
        message['delete'] = "Deleted"

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')
    # The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")


# Delete an archive
class ArchiveDelete(generic.DeleteView):
    model = Archive
    template_name = 'businessCanvas/archive_confirm_delete.html'

    # You need to be connected, and you need to have access
    # as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        company = get_object_or_404(Company, id=self.object.company.id)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(ArchiveDelete, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(ArchiveDelete, self).get_context_data(**kwargs)
        context['company_id'] = kwargs['object'].company.id
        context['archive'] = kwargs['object']
        return context

    # rewrite delete() function to redirect to the good page
    @method_decorator(login_required)
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        company_id = self.object.company.id
        self.object.delete()
        return redirect(reverse_lazy(
            'businessCanvas:businessCanvasElement_list',
            args={company_id}
        ))


# Delete an archive
def deleteArchive(request, archive_id):
    message = {}

    if request.is_ajax():
        archive = Archive.objects.get(id=archive_id)
        elements = archive.elements.filter()
        for element in elements:
            element.delete()
        archive.delete()
        message['delete'] = "Deleted"

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')
    # The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")


# Return detail of an element
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
    # The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")


# Add an element
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

            type_name = request.POST.get('type', '')
            if type_name is None:
                error = True

            company_id = request.POST.get('company', '')
            if company_id is None:
                error = True

            if error is False:
                if(request.POST.get('update', '') == "False"):
                    type = type_name
                    company = Company.objects.get(id=company_id)
                    element = BusinessCanvasElement(
                        title=title,
                        comment=comment,
                        type=type,
                        company=company
                    )
                    element.save()
                    id = element.id
                    return JsonResponse({
                        'type': type_name,
                        'id': id,
                        'title': title,
                        'updated': 'False'
                    })
                else:
                    id = request.POST.get('update', '')
                    element = BusinessCanvasElement.objects.get(id=id)
                    element.title = title
                    element.comment = comment
                    element.save()
                    return JsonResponse({
                        'type': type_name,
                        'id': id,
                        'title': title,
                        'updated': 'True'
                    })
        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")
    # The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")


# Default page, display the current business canvas
class BusinessCanvasElementList(generic.ListView):
    model = BusinessCanvasElement

    # You need to be connected, and you need to have access
    # as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        company = get_object_or_404(Company, id=self.args[0])

        if self.request.user.profile.isCentech():
            return super(BusinessCanvasElementList, self).\
                dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(BusinessCanvasElementList, self).\
                    dispatch(*args, **kwargs)

        if self.request.user.profile.isMentor():
            if company in self.request.user.profile.isMentor().company.all():
                return super(BusinessCanvasElementList, self).\
                    dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(BusinessCanvasElementList, self).\
            get_context_data(**kwargs)
        is_founder = False
        list_founder = Founder.objects.filter(company__pk=self.args[0])
        for founder in list_founder:
            if founder.user.id == self.request.user.id:
                is_founder = True

        context['company_id'] = self.args[0]
        context['company'] = Company.objects.get(id=self.args[0])
        context['is_founder'] = is_founder

        company = Company.objects.get(id=self.args[0])
        archives = Archive.objects.filter(company=company).order_by('date')
        context['archives'] = archives

        for archive in archives:
            context['last_archive'] = archive

        key_partner = BUSINESS_CANVAS_TYPE_CHOICES[0][0]
        list_key_partners = BusinessCanvasElement.objects.filter(
            type=key_partner,
            disactivated=False,
            company=company
        )
        context['list_key_partners'] = list_key_partners

        key_activitie = BUSINESS_CANVAS_TYPE_CHOICES[1][0]
        list_key_activities = BusinessCanvasElement.objects.filter(
            type=key_activitie,
            disactivated=False,
            company=company
        )
        context['list_key_activities'] = list_key_activities

        value_proposition = BUSINESS_CANVAS_TYPE_CHOICES[2][0]
        list_value_propositions = BusinessCanvasElement.objects.filter(
            type=value_proposition,
            disactivated=False,
            company=company
        )
        context['list_value_propositions'] = list_value_propositions

        customer_relationship = BUSINESS_CANVAS_TYPE_CHOICES[3][0]
        list_customer_relationships = BusinessCanvasElement.objects.filter(
            type=customer_relationship,
            disactivated=False,
            company=company
        )
        context['list_customer_relationships'] = list_customer_relationships

        key_resource = BUSINESS_CANVAS_TYPE_CHOICES[4][0]
        list_key_resources = BusinessCanvasElement.objects.filter(
            type=key_resource,
            disactivated=False,
            company=company
        )
        context['list_key_resources'] = list_key_resources

        channel = BUSINESS_CANVAS_TYPE_CHOICES[5][0]
        list_channels = BusinessCanvasElement.objects.filter(
            type=channel,
            disactivated=False,
            company=company
        )
        context['list_channels'] = list_channels

        customer_segment = BUSINESS_CANVAS_TYPE_CHOICES[6][0]
        list_customer_segments = BusinessCanvasElement.objects.filter(
            type=customer_segment,
            disactivated=False,
            company=company
        )
        context['list_customer_segments'] = list_customer_segments

        cost_structure = BUSINESS_CANVAS_TYPE_CHOICES[7][0]
        list_cost_structures = BusinessCanvasElement.objects.filter(
            type=cost_structure,
            disactivated=False,
            company=company
        )
        context['list_cost_structures'] = list_cost_structures

        revenue_stream = BUSINESS_CANVAS_TYPE_CHOICES[8][0]
        list_revenue_streams = BusinessCanvasElement.objects.filter(
            type=revenue_stream,
            disactivated=False,
            company=company
        )
        context['list_revenue_streams'] = list_revenue_streams

        brainstorming_space = BUSINESS_CANVAS_TYPE_CHOICES[9][0]
        list_brainstorming_spaces = BusinessCanvasElement.objects.filter(
            type=brainstorming_space,
            disactivated=False,
            company=company
        )
        context['list_brainstorming_spaces'] = list_brainstorming_spaces

        return context


# Display this archive in a table
class BusinessCanvasElementArchivedList(generic.ListView):
    model = BusinessCanvasElement
    template_name = "businessCanvas/businesscanvaselementarchived_list.html"

    # You need to be connected, and you need to have access
    # as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        archive = get_object_or_404(Archive, id=self.args[0])
        company = get_object_or_404(Company, id=archive.company.id)

        if self.request.user.profile.isCentech():
            return super(BusinessCanvasElementArchivedList, self).\
                dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(BusinessCanvasElementArchivedList, self).\
                    dispatch(*args, **kwargs)

        if self.request.user.profile.isMentor():
            if company in self.request.user.profile.isMentor().company.all():
                return super(BusinessCanvasElementArchivedList, self).\
                    dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        context = super(BusinessCanvasElementArchivedList, self).\
            get_context_data(**kwargs)
        archive = Archive.objects.get(id=self.args[0])
        is_founder = False
        list_founder = Founder.objects.filter(company__pk=archive.company.id)
        for founder in list_founder:
            if founder.user.id == self.request.user.id:
                is_founder = True
        context['company_id'] = archive.company.id
        context['company'] = Company.objects.get(id=archive.company.id)
        context['is_founder'] = is_founder

        context['current_archive'] = archive

        company = archive.company
        archives = Archive.objects.filter(company=company)
        context['archives'] = archives

        key_partner = BUSINESS_CANVAS_TYPE_CHOICES[0][0]
        list_key_partners = archive.elements.filter(
            type=key_partner,
            company=company
        )
        context['list_key_partners'] = list_key_partners

        key_activitie = BUSINESS_CANVAS_TYPE_CHOICES[1][0]
        list_key_activities = archive.elements.filter(
            type=key_activitie,
            company=company
        )
        context['list_key_activities'] = list_key_activities

        value_proposition = BUSINESS_CANVAS_TYPE_CHOICES[2][0]
        list_value_propositions = archive.elements.filter(
            type=value_proposition,
            company=company
        )
        context['list_value_propositions'] = list_value_propositions

        customer_relationship = BUSINESS_CANVAS_TYPE_CHOICES[3][0]
        list_customer_relationships = archive.elements.filter(
            type=customer_relationship,
            company=company
        )
        context['list_customer_relationships'] = list_customer_relationships

        key_resource = BUSINESS_CANVAS_TYPE_CHOICES[4][0]
        list_key_resources = archive.elements.filter(
            type=key_resource,
            company=company
        )
        context['list_key_resources'] = list_key_resources

        channel = BUSINESS_CANVAS_TYPE_CHOICES[5][0]
        list_channels = archive.elements.filter(
            type=channel,
            company=company
        )
        context['list_channels'] = list_channels

        customer_segment = BUSINESS_CANVAS_TYPE_CHOICES[6][0]
        list_customer_segments = archive.elements.filter(
            type=customer_segment,
            company=company
        )
        context['list_customer_segments'] = list_customer_segments

        cost_structure = BUSINESS_CANVAS_TYPE_CHOICES[7][0]
        list_cost_structures = archive.elements.filter(
            type=cost_structure,
            company=company
        )
        context['list_cost_structures'] = list_cost_structures

        revenue_stream = BUSINESS_CANVAS_TYPE_CHOICES[8][0]
        list_revenue_streams = archive.elements.filter(
            type=revenue_stream,
            company=company
        )
        context['list_revenue_streams'] = list_revenue_streams

        brainstorming_space = BUSINESS_CANVAS_TYPE_CHOICES[9][0]
        list_brainstorming_spaces = archive.elements.filter(
            type=brainstorming_space,
            company=company
        )
        context['list_brainstorming_spaces'] = list_brainstorming_spaces

        return context
