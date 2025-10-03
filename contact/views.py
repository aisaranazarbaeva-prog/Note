from django.shortcuts import render
from rest_framework import generics
from .serializer import NewSerializer
from .models import Contacts



class NewContact(generics.ListCreateAPIView):
    serializer_class = NewSerializer


class  NewDetailContactAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewSerializer
    queryset = Contacts.objects.all()

# Create your views here.
