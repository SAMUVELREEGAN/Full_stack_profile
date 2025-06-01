from django.contrib import admin
from .models import MyContact, AutoReplyMessage

@admin.register(MyContact)
class MyContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone']

@admin.register(AutoReplyMessage)
class AutoReplyMessageAdmin(admin.ModelAdmin):
    list_display = ('form_type', 'message')
