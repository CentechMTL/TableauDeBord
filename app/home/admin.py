# coding: utf-8

from django.contrib import admin

from app.home.models import UserProfile, Education, Expertise


class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['image_thumb']


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['image_thumb']

admin.site.register(Expertise)
admin.site.register(Education)
admin.site.register(UserProfile)
