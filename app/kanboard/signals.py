import datetime
import django.dispatch

phase_change = django.dispatch.Signal(
    providing_args=[
        'from_phase',
        'to_phase',
        'changed_at'
    ]
)


def card_order(sender, instance, **kwargs):
    if instance.order:
        return

    from app.kanboard.models import Card
    instance.order = len(Card.objects.filter(phase=instance.phase)) + 1
