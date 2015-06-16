from django.contrib import admin
from app.kanboard.models import Phase, Card

class CardAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


admin.site.register(Card, CardAdmin)
admin.site.register(Phase)

