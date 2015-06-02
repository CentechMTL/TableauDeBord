# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from app.home.models import UserProfile,Education,Expertise
from app.company.models import Company,CompanyStatus
from app.kpi.models import KPI
from app.home.forms import UserForm

class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['image_thumb']

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['image_thumb']


#admin.site.register(Question,QuestionAdmin)
admin.site.register(Expertise)
admin.site.register(Education)



