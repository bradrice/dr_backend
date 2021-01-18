from django.shortcuts import render
from .models import AboutPageContent
from .serializers import AboutPageSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response


# Create your views here.
class AboutPageDetail(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = AboutPageContent.objects.all()
    serializer_class = AboutPageSerializer