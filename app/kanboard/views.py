import re
from django import http
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from app.kanboard.models import Board, Card, Phase, PhaseLog, KanboardStats
from app.company.models import Company
from app.founder.models import Founder
from app.mentor.models import Mentor

from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

PHASE_RE = re.compile(u'^phase-([\d]+)\[\]$')
CARD_RE = re.compile(u'^card-([\d]+)$')

class BoardIndex(TemplateView):
    template_name = 'kanboard/board.html'

    def get_context_data(self, **kwargs):
        company = Company.objects.get(id = int(kwargs['pk']))
        board = company.board.all()[0]
        context = super(BoardIndex, self).get_context_data(**kwargs)
        context['company'] = company
        context['board'] = board
        return context


#Update the kanboard
def update(request, id):
    updates = []
    if request.is_ajax():
        try:
            company = Company.objects.get(id = id)
            board = get_object_or_404(Board, company=company)

            #Verify data and create a tmp list of cards and phases
            for phase_name, card_names in request.POST.lists():
                cards = []
                phase_match = PHASE_RE.match(phase_name) #Regex to verify data
                if not phase_match:
                    raise Exception("Malformed phase_name: <%s>" % phase_name)
                phase = get_object_or_404(Phase, board=board, pk=int(phase_match.group(1)))

                #Listing of cards in the phase
                for card_name in card_names:
                    card_match = CARD_RE.match(card_name) #Regex to verify data
                    if not card_match:
                        raise Exception("Malformed card_name: <%s>" % card_name)
                    card = get_object_or_404(Card, phase__board=board, pk=int(card_match.group(1)))
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
