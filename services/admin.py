from django.contrib import admin
from .models import Service


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created_date', 'update_date')


admin.site.register(Service, ServiceAdmin)

