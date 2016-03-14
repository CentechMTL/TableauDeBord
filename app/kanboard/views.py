import re
import time
from django import http
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from app.kanboard.models import Card, Comment, PHASE_CHOICES
from app.company.models import Company
from app.founder.models import Founder
from app.mentor.models import Mentor
from django.contrib.auth.models import User

from app.kanboard.forms import CardForm

from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import json

PHASE_RE = re.compile(u'^phase-([\d]+)\[\]$')
CARD_RE = re.compile(u'^card-([\d]+)$')


# Return detail of a kanboard
def getDetailKanboard(request, company_id, state):
    if request.is_ajax():
        message = []

        if state == 'true':
            state = True
        elif state == 'false':
            state = False
        else:
            state = None

        for phaseLoop in PHASE_CHOICES:
            phase = {}
            cards = Card.objects.filter(
                phase=phaseLoop[1],
                company=company_id
            )
            for card in cards:
                if state == card.state:
                    phase[card.id] = card.id
                elif state is None:
                    phase[card.id] = card.id
            tuple = (phaseLoop[1], phase)
            message.append(tuple)

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')

    # The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")


# Return detail of a card
def getDetailCard(request, card_id):
    message = {}

    if request.is_ajax():
        try:
            card = Card.objects.get(id=card_id)

            message['title'] = card.title
            message['comment'] = card.comment
            message['state'] = card.state

            for phase in PHASE_CHOICES:
                if phase[1] == card.phase:
                    message['phase'] = phase[0]

            message['id'] = card.id
            message['creator'] = card.creator.username

            if card.assigned:
                message['assigned'] = card.assigned.userProfile_id
                message['picture'] = str(card.assigned.picture)

            if card.deadline:
                message['deadline'] = card.deadline.strftime('%Y-%m-%d')

        except:
            pass
        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')

    # The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")


# Add a card
def addCard(request, id):
    if request.is_ajax():
        if request.method == "POST":
            error = False

            # We take data
            title = request.POST.get('title', '')
            if title is None or title == "":
                error = True

            comment = request.POST.get('comment', '')
            if comment is None:
                comment = ""

            deadline = request.POST.get('deadline', '')
            assigned = request.POST.get('assigned', '')
            order = request.POST.get('order', '')
            update = request.POST.get('update', '')

            phase = request.POST.get('phase', '')
            try:
                phase = int(phase)
                exist = False
                print phase
                for elem in PHASE_CHOICES:
                    print elem[0]
                    if elem[0] == int(phase):
                        exist = True
                if not exist:
                    error = True
            except:
                error = True

            state = request.POST.get('state', '')
            if state == 'false':
                state = False
            else:
                state = True

            # If we have all data
            if not error:
                # If it's a new card
                if(update == 'False'):
                    pictureAssigned = False
                    phase = PHASE_CHOICES[phase-1]
                    company = Company.objects.get(id=id)

                    card = Card(
                        title=title,
                        company=company,
                        comment=comment,
                        creator=request.user,
                        phase=phase[1],
                        order=order,
                        state=state
                    )

                    if deadline != "":
                        card.deadline = deadline
                    if assigned != "":
                        founder = Founder.objects.get(userProfile_id=assigned)
                        card.assigned = founder
                        pictureAssigned = str(founder.picture)
                    else:
                        card.assigned = None
                    card.save()
                    id = card.id
                    return JsonResponse(
                        {
                            'phase': phase[0],
                            'company': company.id,
                            'id': id,
                            'title': title,
                            'comment': comment,
                            'updated': False,
                            'picture': pictureAssigned,
                            'assigned': assigned,
                        }
                    )

                # If it's an update of a card
                else:
                    pictureAssigned = False
                    phase = PHASE_CHOICES[phase-1]
                    company = Company.objects.get(id=id)

                    card = Card.objects.get(id=update)
                    card.title = title
                    card.state = state
                    card.comment = comment
                    card.phase = phase[1]
                    card.company = company
                    if deadline != "":
                        card.deadline = deadline
                    else:
                        card.deadline = None
                    if assigned != "":
                        founder = Founder.objects.get(userProfile_id=assigned)
                        card.assigned = founder
                        pictureAssigned = str(founder.picture)
                    else:
                        card.assigned = None
                    card.save()
                    return JsonResponse({'phase': phase[0],
                                         'company': company.id,
                                         'id': update,
                                         'title': title,
                                         'comment': comment,
                                         'updated': True,
                                         'picture': pictureAssigned,
                                         'assigned': assigned
                                         })

    # The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")


# Delete a card of the kanboard
def deleteCard(request, card_id):
    message = {}

    if request.is_ajax():
        card = Card.objects.get(id=card_id)
        card.delete()
        message['delete'] = "Deleted"

        data = json.dumps(message)
        return HttpResponse(data, content_type='application/json')
    # The visitor can't see this page!
    return HttpResponseRedirect("/user/noAccessPermissions")


# Update the kanboard
def update(request, id):
    updates = []
    if request.is_ajax():
        try:
            company = Company.objects.get(id=id)

            # Verify data and create a tmp list of cards and phases
            for phase_name, card_names in request.POST.lists():
                cards = []
                # Regex to verify data
                phase_match = PHASE_RE.match(phase_name)
                if not phase_match:
                    raise Exception("Malformed phase_name: <%s>" % phase_name)
                phase = PHASE_CHOICES[int(phase_match.group(1))-1]

                # Listing of cards in the phase
                for card_name in card_names:
                    # Regex to verify data
                    card_match = CARD_RE.match(card_name)
                    if not card_match:
                        raise Exception(
                            "Malformed card_name: <%s>" % card_name
                        )
                    card = get_object_or_404(Card, pk=int(card_match.group(1)))
                    cards.append(card)
                updates.append((phase[1], cards))

                # Update phase of cards
                for phase, cards in updates:
                    for card in cards:
                        if card.phase != phase:
                            card.change_phase(phase)

                # Update order of cards
                for phase, cards in updates:
                    for i, card in enumerate(cards):
                        card.order = i+1
                        card.save()

        except Exception, e:
            print "Exception: %s, %r" % (e, e)
            raise

    return http.HttpResponse()  # nothing exciting...


# Add a card
def addComment(request, id):
    if request.is_ajax():
        if request.method == "POST":
            error = False

            # We take data
            comment = request.POST.get('comment', '')
            if comment is None or comment == "":
                error = True

            # If we have all data
            if not error:
                comment = Comment(
                    comment=comment,
                    card=Card.objects.get(id=id),
                    creator=request.user
                )

                comment.save()

                return JsonResponse(
                    {
                        'comment': comment.comment,
                        'creator': comment.creator.username,
                        'created': comment.created.strftime("%Y/%m/%d"),
                        'id': comment.id,
                    }
                )


class BoardIndex(generic.TemplateView):
    template_name = 'kanboard/board.html'

    # You need to be connected, and you need to have access
    # as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        company = get_object_or_404(Company, id=int(kwargs['pk']))

        if self.request.user.profile.isCentech():
            return super(BoardIndex, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(BoardIndex, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isMentor():
            if company in self.request.user.profile.isMentor().company.all():
                return super(BoardIndex, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")

    def get_context_data(self, **kwargs):
        company = Company.objects.get(id=int(kwargs['pk']))

        context = super(BoardIndex, self).get_context_data(**kwargs)
        context['company'] = company
        context['form'] = CardForm(company)

        return context


# Display detail of the company
class CardView(generic.DetailView):
    model = Card
    template_name = 'kanboard/card.html'

    # You need to be connected, and you need to have access
    # as founder, mentor or Centech
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        card = get_object_or_404(Card, id=int(kwargs['pk']))
        company = get_object_or_404(Company, id=card.company.id)

        if self.request.user.profile.isCentech():
            return super(CardView, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isFounder():
            if company in self.request.user.profile.isFounder().company.all():
                return super(CardView, self).dispatch(*args, **kwargs)

        if self.request.user.profile.isMentor():
            if company in self.request.user.profile.isMentor().company.all():
                return super(CardView, self).dispatch(*args, **kwargs)

        # The visitor can't see this page!
        return HttpResponseRedirect("/user/noAccessPermissions")
