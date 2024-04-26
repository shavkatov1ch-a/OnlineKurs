from django.urls import path

import contact
from .views import *

urlpatterns = [
    path('contact/', ContactAPIView.as_view(), name='contact'),
    path('about/', AboutAPIView.as_view(), name='about'),
]