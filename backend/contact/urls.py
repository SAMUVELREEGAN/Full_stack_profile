from django.urls import path
from .views import *

urlpatterns = [
    path('', MyContactView.as_view(), name='mycontact'),
   path('contact/', contact_form_view),
]
