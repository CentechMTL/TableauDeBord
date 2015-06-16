import datetime
from django.utils import timezone

from django.db import models

from app.kanboard import signals
from app.company.models import Company

class Phase(models.Model):
    UPCOMING = 'upcoming'
    PROGRESS = 'progress'
    FINISHED = 'finished'
    STATUSES = (
        (UPCOMING, 'Upcoming'),
        (PROGRESS, 'In progress'),
        (FINISHED, 'Finished'),
    )

    title = models.CharField(max_length=80)
    company = models.ForeignKey(Company, related_name="phases")
    # Order of the phase within the board:
    order = models.SmallIntegerField()
    # The status is used to determine whether the phase is WIP or not (for
    # stats calculation):
    status = models.CharField(max_length=25, choices=STATUSES,
                              default=PROGRESS)

    #Optional fields
    description = models.TextField(blank=True)
    limit = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return u"%s - %s (%s)" % (self.company.name, self.title, self.order)


class Card(models.Model):
    """
    A card is a specific piece of work which must be done on a project, which
    can be hung on a "board" (under a specific "phase").
    """
    title = models.CharField(max_length=80)
    comment = models.TextField(blank=True)
    deadline = models.DateField(blank=True, null=True)

    phase = models.ForeignKey(Phase, related_name="cards")

    order = models.SmallIntegerField()

    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(blank=True)

    class Meta:
        ordering = ['order', ]

    def __unicode__(self):
        return "%s - %s (%s) -- %s" % (self.id, self.title, self.order, self.phase.title)

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

#SIGNALS CONNECTED
models.signals.pre_save.connect(signals.card_order, sender=Card)