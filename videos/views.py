from django.shortcuts import render
from rest_framework import viewsets
from .serializer import NewsSerializer
from .models import Videoss

class NewsViewSet(viewsets.ModelViewSet):
    queryset = Videoss.objects.all()
    serializer_class = NewsSerializer

