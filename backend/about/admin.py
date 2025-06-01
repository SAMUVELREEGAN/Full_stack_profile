from django.contrib import admin
from django.utils.html import format_html
from .models import About, AboutList

class AboutListInline(admin.TabularInline):
    model = AboutList
    extra = 1

class AboutAdmin(admin.ModelAdmin):
    inlines = [AboutListInline]
    list_display = ('display_image', 'name')  # show image + name in list view

    def display_image(self, obj):
        if obj.pic:
            return format_html('<img src="{}" width="60" height="60" style="object-fit: cover;" />', obj.pic.url)
        return "No Image"

    display_image.short_description = "Image"

admin.site.register(About, AboutAdmin)
