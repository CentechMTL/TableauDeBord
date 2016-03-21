# coding: utf-8

from celery import shared_task

from django.core.management import call_command


@shared_task
def update_floor_map():
    return call_command('updateFloorMap')
