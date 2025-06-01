from django.urls import path
from .views import *

urlpatterns = [
    path('', LandingParaList.as_view(), name='landing-para'),
    path('theme-settings', ThemeSettingsView.as_view(), name='landing-para'),
]
