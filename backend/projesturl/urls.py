from django.urls import path
from .views import ProjectList

urlpatterns = [
    path('projectsurls/', ProjectList.as_view(), name='project-list'),
]
