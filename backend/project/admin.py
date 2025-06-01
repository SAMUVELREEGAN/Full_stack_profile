from django.contrib import admin

from django.utils.html import format_html
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'language', 'link_name', 'image_tag']  # ✅ Add image_tag
    readonly_fields = ['image_tag']  # ✅ Optional: show in detail view too

    def image_tag(self, obj):
        if obj.pic:
            return format_html('<img src="{}" width="80" style="border-radius:4px;" />', obj.pic.url)
        return "No Image"

    image_tag.short_description = 'Preview'

