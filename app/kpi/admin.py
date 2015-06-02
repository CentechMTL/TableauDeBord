from django.contrib import admin
from app.kpi.models import KPI, KpiType

admin.site.register(KPI)
admin.site.register(KpiType)