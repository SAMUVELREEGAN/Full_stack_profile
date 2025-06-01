from django.urls import path
from .views import MyskillListAPIView

urlpatterns = [
    path('', MyskillListAPIView.as_view(), name='myskill-list'),
]
