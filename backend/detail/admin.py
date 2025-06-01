from django.contrib import admin
from .models import Detail
from django.utils.html import format_html

class DetailAdmin(admin.ModelAdmin):
    list_display = ('display_pic1', 'display_pic2', 'mynamebeAfter', 'role')

    def display_pic1(self, obj):
        if obj.mypic1:
            return format_html('<img src="{}" width="60" height="60" />', obj.mypic1.url)
        return "No Image"

    def display_pic2(self, obj):
        if obj.mypic2:
            return format_html('<img src="{}" width="60" height="60" />', obj.mypic2.url)
        return "No Image"

    display_pic1.short_description = "Image 1"
    display_pic2.short_description = "Image 2"

admin.site.register(Detail, DetailAdmin)
