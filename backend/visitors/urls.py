# urls.py
from django.urls import path
from .views import VisitorCreateAPIView

urlpatterns = [
    path('', VisitorCreateAPIView.as_view(), name='visitor-create'),
]
