from django.contrib import admin
from .models import Service


# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_name', 'slug', 'small_service_description', 'service_description', 'price', 'category', 'modified_date', 'is_available')
    prepopulated_fields={'slug':('service_name',)}

admin.site.register(Service, ServiceAdmin)
