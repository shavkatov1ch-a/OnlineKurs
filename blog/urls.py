from collections import UserList

from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UsersAPIView.as_view(), name='users'),
    path('video_kurslar/', VideoDarslarAPIView.as_view(), name='video_kurslar'),
    path('team/', TeamAPIView.as_view(), name='team'),
    path('web-sites/', Web_sitesAPIView.as_view(), name='web_sites'),
    path('web-images/', Web_imagesAPIView.as_view(), name='web_images'),
    path('payment/', PaymentAPIView.as_view(), name='payment'),
    path('clients/', ClientAPIView.as_view(), name='clients'),
]