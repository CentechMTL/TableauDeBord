# coding: utf-8

from django.contrib import admin
from app.mentor.models import Mentor


class MentorAdmin(admin.ModelAdmin):
    readonly_fields = ['image_thumb']

admin.site.register(Mentor, MentorAdmin)
