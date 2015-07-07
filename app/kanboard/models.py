import datetime
from django.utils import timezone

from django.db import models

from app.kanboard import signals
from app.company.models import Company
from app.founder.models import Founder
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _

PHASE_CHOICES = (
    (1, u'Finance'),
    (2, u'R&D'),
    (3, u'Centech'),
)

class Card(models.Model):
    """
    A card is a specific piece of work which must be done on a project, which
    can be hung on a "board" (under a specific "phase").
    """
    title = models.CharField(max_length=80)
    comment = models.TextField(blank=True)
    deadline = models.DateField(blank=True, null=True)
    company = models.ForeignKey(Company, related_name="cards")
    phase = models.CharField(max_length=50, choices=PHASE_CHOICES, verbose_name=_('Phase'))
    order = models.SmallIntegerField()

    assigned = models.ForeignKey(Founder, related_name="cards_assigned", blank=True, null=True)
    creator = models.ForeignKey(User, related_name="cards_create", blank=True, null=True)

    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['order', ]

    def __unicode__(self):
        return "%s -- %s" % (self.title, self.company)

    def save(self, *args, **kwarg):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        super(Card, self).save(*args, **kwarg)

    def change_phase(self, new_phase, change_at=None):
        from_phase = self.phase
        self.phase = new_phase
        self.save()

        signals.phase_change.send(sender=self, from_phase=from_phase,
                                  to_phase=new_phase, changed_at=change_at)

    def is_past_due(self):
        if(self.deadline):
            if datetime.date.today() > self.deadline:
                return True
        return False

#SIGNALS CONNECTED
models.signals.pre_save.connect(signals.card_order, sender=Card)