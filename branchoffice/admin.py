from django.contrib import admin
from .models import BranchOffice


# Register your models here.

class BranchOfficeAdmin(admin.ModelAdmin):
    list_display=('branch_office_name', 'branch_office_address', 'modified_date', 'is_available')

admin.site.register(BranchOffice, BranchOfficeAdmin)
