from django.contrib import admin
from .models import EducationGroup, EducationItem

class EducationItemInline(admin.TabularInline):
    model = EducationItem
    extra = 1

class EducationGroupAdmin(admin.ModelAdmin):
    inlines = [EducationItemInline]

admin.site.register(EducationGroup, EducationGroupAdmin)
