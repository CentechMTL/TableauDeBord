import datetime

import django.dispatch

phase_change = django.dispatch.Signal(providing_args=['from_phase', 'to_phase', 'changed_at'])

def card_order(sender, instance, **kwargs):
    if instance.order:
        return
    from django.db.models import Max
    max_order = instance.phase.cards.aggregate(
                                max_order=Max('order'))['max_order']
    instance.order = max_order and max_order + 1 or 1
