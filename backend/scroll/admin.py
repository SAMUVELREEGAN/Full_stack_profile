from django.contrib import admin
from .models import Scroll

@admin.register(Scroll)
class ScrollAdmin(admin.ModelAdmin):
    list_display = ('scname',)
