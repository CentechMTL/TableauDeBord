# coding: utf-8
from django.contrib import admin
from app.company.models import Founder


class FounderAdmin(admin.ModelAdmin):

    # Configuration of the list
    list_display = ('user', 'equity',)
    list_filter = ('user', 'equity', 'education', 'expertise',)
    search_fields = ('user', 'equity', 'education', 'expertise',)

    # Configuration of the edit form
    readonly_fields = ['image_thumb']
    fieldsets = (
        # Fieldset 1 : meta-info
        ('Profil', {
            'description': u'General informations:',
            'fields': ('user', 'phone', 'website', 'picture', 'image_thumb',),

        }),
        # Fieldset 2 : promotion information
        ('Promotion', {
           'description': u'This information is the one present on '
                          u'the presentation page!',
           'fields': ('about',)
        }),
        # Fieldset 3 : centech
        ('Details', {
           'fields': ('equity', 'education', 'expertise',)
        }),
    )

admin.site.register(Founder, FounderAdmin)
