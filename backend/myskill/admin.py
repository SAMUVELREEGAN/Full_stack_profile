from django.contrib import admin
from .models import Myskill
from django.utils.html import format_html
from django.contrib import admin

@admin.register(Myskill)
class MyskillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'rangecolor', 'preview')

    def preview(self, obj):
        if obj.pic:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.pic.url)
        return "-"
    
    preview.short_description = 'Image'
