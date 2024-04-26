from django.shortcuts import render
from rest_framework import generics
from .models import Contact, About
from .serializers import ContactSerializer, AboutSerializer

class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class AboutAPIView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
