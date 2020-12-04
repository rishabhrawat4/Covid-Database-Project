from django.contrib import admin
from .models import Drug
from import_export.admin import ImportExportModelAdmin

@admin.register(Drug)
class DrugAdmin(ImportExportModelAdmin):
    pass