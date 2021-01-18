from django.shortcuts import render
from .models import HomePageContent
from .serializers import HomePageSerializer
from rest_framework import generics
from rest_framework import permissions

# Create your views here.
class HomePageDetail(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = HomePageContent.objects.all()
    serializer_class = HomePageSerializer