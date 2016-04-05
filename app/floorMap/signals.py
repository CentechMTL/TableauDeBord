# coding: utf-8

from django.core.management import call_command


def update_floor_map(sender, **kwargs):
    call_command('updateFloorMap')
