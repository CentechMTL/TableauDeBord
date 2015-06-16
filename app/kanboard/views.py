import re
from django import http
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from app.kanboard.models import Card, Phase
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
            message['phase'] = card.phase.id
            message['id'] = card.id
            message['deadline'] = card.deadline.strftime('%Y-%m-%d')
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
            if deadline == None:
                deadline = ""

            order = request.POST.get('order', '')
            update = request.POST.get('update', '')

            if error == False:
                if(update == 'False'):
                    phase = Phase.objects.get(id = id)
                    card = Card(title = title, comment = comment, phase = phase, order = order, deadline = deadline)
                    card.save()
                    id = card.id
                    return JsonResponse({'phase': phase.id, 'id': id, 'title': title, 'comment': comment, 'updated': False})
                else:
                    phase = Phase.objects.get(id = id)
                    card = Card.objects.get(id = update)
                    card.title = title
                    card.comment = comment
                    card.phase = phase
                    card.deadline = deadline
                    card.order = order
                    card.save()
                    return JsonResponse({'phase': phase.id, 'id': update, 'title': title, 'comment': comment, 'updated': True})

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

    def get_context_data(self, **kwargs):
        company = Company.objects.get(id = int(kwargs['pk']))
        context = super(BoardIndex, self).get_context_data(**kwargs)
        context['company'] = company

        context['form'] = CardForm(company)
        return context


#Update the kanboard
def update(request, id):
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
                phase = get_object_or_404(Phase, pk=int(phase_match.group(1)))

                #Listing of cards in the phase
                for card_name in card_names:
                    card_match = CARD_RE.match(card_name) #Regex to verify data
                    if not card_match:
                        raise Exception("Malformed card_name: <%s>" % card_name)
                    card = get_object_or_404(Card, pk=int(card_match.group(1)))
                    cards.append(card)
                updates.append((phase, cards))
                updates.sort(cmp=lambda x,y: cmp(x[0].order, y[0].order))

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
