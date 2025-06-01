from django.urls import path
from .views import *

urlpatterns = [
    path('send-feedback/', send_feedback, name='send-feedback'),
    path('social-links/', SocialLinksAPIView.as_view(), name='social-links'),
]
