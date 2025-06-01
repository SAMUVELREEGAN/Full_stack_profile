from django.urls import path
from .views import EducationGroupView

urlpatterns = [
    path('', EducationGroupView.as_view(), name='education'),
]
