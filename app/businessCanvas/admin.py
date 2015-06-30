# coding: utf-8

from django.contrib import admin
from app.businessCanvas.models import BusinessCanvasElement, Archive

admin.site.register(BusinessCanvasElement)
admin.site.register(Archive)