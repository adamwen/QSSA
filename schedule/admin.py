import models
from django.contrib import admin
from schedule.models import Info

class InfoAdmin(admin.ModelAdmin):
    list_display = ('schoolId', 'pw', 'email', 'password')

admin.site.register(Info, InfoAdmin)
