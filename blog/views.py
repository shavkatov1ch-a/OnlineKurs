from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Users, Video_Darslar, Team, Web_sites, Web_images, Payment, Client
from .serializers import *


class UsersAPIView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer



class VideoDarslarAPIView(generics.ListAPIView):
    queryset = Video_Darslar.objects.all()
    serializer_class = Video_DarslarSerializer
    permission_classes = [permissions.IsAuthenticated, Client.is_pay]

    def process_payment(self, is_pay):
        try:
            lesson = Client.objects.get(pk=is_pay['lesson'])
        except Client.DoesNotExist:
            return HttpResponse(status=400)


        lesson.is_pay = True
        lesson.save()

        serializer = ClientSerializer(lesson)
        return HttpResponse(serializer.data)



class TeamAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class Web_sitesAPIView(generics.ListAPIView):
    queryset = Web_sites.objects.all()
    serializer_class = Web_sitesSerializer


class Web_imagesAPIView(generics.ListAPIView):
    queryset = Web_images.objects.all()
    serializer_class = Web_imagesSerializer


class PaymentAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ClientAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer