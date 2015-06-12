import re
from django import http
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from app.kanboard import models, forms

PHASE_RE = re.compile(u'^phase-([\d]+)\[\]$')
CARD_RE = re.compile(u'^card-([\d]+)$')

#The main page, display all card on all phases
def board(request, board_slug, template_name='kanboard/board.html'):
    board = get_object_or_404(models.Board, slug=board_slug)
    return render_to_response(template_name, dict(board=board, context_instance=RequestContext(request)))

#Update the kanboard
def update(request, board_slug):
    updates = []
    if request.is_ajax():
        try:
            board = get_object_or_404(models.Board, slug=board_slug)

            #Verify data and create a tmp list of cards and phases
            for phase_name, card_names in request.POST.lists():
                cards = []
                phase_match = PHASE_RE.match(phase_name) #Regex to verify data
                if not phase_match:
                    raise Exception("Malformed phase_name: <%s>" % phase_name)
                phase = get_object_or_404(models.Phase, board=board, pk=int(phase_match.group(1)))

                #Listing of cards in the phase
                for card_name in card_names:
                    card_match = CARD_RE.match(card_name) #Regex to verify data
                    if not card_match:
                        raise Exception("Malformed card_name: <%s>" % card_name)
                    card = get_object_or_404(models.Card, phase__board=board, pk=int(card_match.group(1)))
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
