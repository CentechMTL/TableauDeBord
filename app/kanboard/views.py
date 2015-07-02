import re
from django import http
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from app.kanboard.models import Card, PHASE_CHOICES
from app.company.models import Company
from app.founder.models import Founder
from app.mentor.models import Mentor

from app.kanboard.forms import CardForm

from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import json

PHASE_RE = re.compile(u'^phase-([\d]+)\[\]$')
CARD_RE = re.compile(u'^card-([\d]+)$')

#Return detail of a card
def getDetailCard(request, card_id):
    message = {}

    if request.is_ajax():
        try:
            card = Card.objects.get(id=card_id)

            message['title'] = card.title
            message['comment'] = card.comment


            for phase in PHASE_CHOICES:
                if phase[1] == card.phase:
                    message['phase'] = phase[0]

            message['id'] = card.id
            message['deadline'] = card.deadline.strftime('%Y-%m-%d')
            message['assigned'] = card.assigned.userProfile_id
            if card.assigned:
                message['picture'] = str(card.assigned.picture)
        except:
            pass
        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')

    #The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")

#Add a card
def addCard(request, id):
    if request.is_ajax():
        if request.method == "POST":
            error = False

            title = request.POST.get('title', '')
            if title == None or title == "":
                error = True

            comment = request.POST.get('comment', '')
            if comment == None:
                comment = ""

            deadline = request.POST.get('deadline', '')
            assigned = request.POST.get('assigned', '')
            order = request.POST.get('order', '')
            update = request.POST.get('update', '')
            phase = request.POST.get('phase', '')
            company = request.POST.get('company', '')

            if error == False:
                if(update == 'False'):
                    pictureAssigned = False
                    phase = PHASE_CHOICES[int(phase)-1]
                    company = Company.objects.get(id = company)

                    card = Card(title = title, company = company, comment = comment, phase = phase[1], order = order)
                    if deadline != "":
                        card.deadline = deadline
                    if assigned != "":
                        founder = Founder.objects.get(userProfile_id = assigned)
                        card.assigned = founder
                        pictureAssigned = str(founder.picture)
                    else:
                        card.assigned = None
                    card.save()
                    id = card.id
                    return JsonResponse({'phase': phase[0], 'company': company.id, 'id': id, 'title': title, 'comment': comment, 'updated': False, 'picture': pictureAssigned, 'assigned': assigned})
                else:
                    pictureAssigned = False
                    phase = PHASE_CHOICES[int(phase)-1]
                    company = Company.objects.get(id = company)

                    card = Card.objects.get(id = update)
                    card.title = title
                    card.comment = comment
                    card.phase = phase[1]
                    card.company = company
                    if deadline != "":
                        card.deadline = deadline
                    if assigned != "":
                        founder = Founder.objects.get(userProfile_id = assigned)
                        card.assigned = founder
                        pictureAssigned = str(founder.picture)
                    else:
                        card.assigned = None
                    card.order = order
                    card.save()
                    return JsonResponse({'phase': phase[0], 'company': company.id, 'id': update, 'title': title, 'comment': comment, 'updated': True, 'picture': pictureAssigned, 'assigned': assigned})

    #The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")

#Delete a card of the kanboard
def deleteCard(request, card_id):
    message= {}

    if request.is_ajax():
        card = Card.objects.get(id = card_id)
        card.delete()
        message['delete'] = "Deleted"

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')
    #The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")

class BoardIndex(TemplateView):
    template_name = 'kanboard/board.html'

    #You need to be connected, and you need to have access as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        #For know if the user is in the group "Centech"
        groups = self.request.user.groups.values()
        for group in groups:
            if group['name'] == 'Centech':
                try:
                    company = Company.objects.get(id = int(kwargs['pk'])) #If the company exist, else we go to except
                    return super(BoardIndex, self).dispatch(*args, **kwargs)
                except:
                    pass

        #For know the company of the user if is a founder
        if self.request.user.is_active:
            try:
                founder = Founder.objects.filter(user = self.request.user.id)
                company = Company.objects.get(founders = founder)
                if(int(kwargs['pk']) == int(company.id)):
                    return super(BoardIndex, self).dispatch(*args, **kwargs)
            except:
                pass

        #For know the company of the user if is a mentor
        if self.request.user.is_active:
            try:
                mentor = Mentor.objects.filter(user = self.request.user.id)
                company = Company.objects.get(mentors = mentor)
                if(int(kwargs['pk']) == int(company.id)):
                    return super(BoardIndex, self).dispatch(*args, **kwargs)
            except:
                pass

        #The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        company = Company.objects.get(id = int(kwargs['pk']))

        context = super(BoardIndex, self).get_context_data(**kwargs)
        context['company'] = company
        context['phases'] = PHASE_CHOICES

        context['form'] = CardForm(company)
        return context


#Update the kanboard
def update(request, id):
    print('update')
    updates = []
    if request.is_ajax():
        try:
            company = Company.objects.get(id = id)

            #Verify data and create a tmp list of cards and phases
            for phase_name, card_names in request.POST.lists():
                cards = []
                phase_match = PHASE_RE.match(phase_name) #Regex to verify data
                if not phase_match:
                    raise Exception("Malformed phase_name: <%s>" % phase_name)
                phase = PHASE_CHOICES[int(phase_match.group(1))-1]

                #Listing of cards in the phase
                for card_name in card_names:
                    card_match = CARD_RE.match(card_name) #Regex to verify data
                    if not card_match:
                        raise Exception("Malformed card_name: <%s>" % card_name)
                    card = get_object_or_404(Card, pk=int(card_match.group(1)))
                    cards.append(card)
                updates.append((phase[1], cards))

                #Update phase of cards
                for phase, cards in updates:
                    for card in cards:
                        if card.phase != phase:
                            card.change_phase(phase)

                #Update order of cards
                for phase, cards in updates:
                    for i, card in enumerate(cards):
                        card.order = i+1
                        card.save()

        except Exception, e:
            print "Exception: %s, %r" % (e, e)
            raise

    return http.HttpResponse() # nothing exciting...
