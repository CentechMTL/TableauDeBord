# coding: utf-8

from django.contrib import admin

from app.floorMap.models import Room, RoomType, Rent


class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['image_thumb']


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['image_thumb']

admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Rent)
