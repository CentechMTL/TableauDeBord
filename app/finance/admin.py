from django.contrib import admin
from app.finance.models import Bourse, Subvention, Investissement, Pret, Vente

admin.site.register(Bourse)
admin.site.register(Subvention)
admin.site.register(Investissement)
admin.site.register(Pret)
admin.site.register(Vente)