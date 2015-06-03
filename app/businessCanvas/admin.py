# coding: utf-8

from django.contrib import admin
from app.businessCanvas.models import BusinessCanvasElement, BusinessCanvasType, Archive

admin.site.register(BusinessCanvasType)
admin.site.register(BusinessCanvasElement)
admin.site.register(Archive)