from django.contrib import admin
from .models import Experience

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'role', 'location', 'duration')
    search_fields = ('company_name', 'role', 'location')
