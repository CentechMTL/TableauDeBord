# coding: utf-8

from django.contrib import admin
from app.valuePropositionCanvas.models import ValuePropositionCanvasElement, ValuePropositionCanvasType

admin.site.register(ValuePropositionCanvasElement)
admin.site.register(ValuePropositionCanvasType)