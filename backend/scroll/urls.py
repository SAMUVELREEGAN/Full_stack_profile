from django.urls import path
from .views import ScrollListAPIView

urlpatterns = [
    path('', ScrollListAPIView.as_view(), name='scroll-list'),
]
