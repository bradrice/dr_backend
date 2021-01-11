from django.shortcuts import render
from .models import Carousel
from .serializers import CarouselSerializer
from rest_framework import generics
from rest_framework import permissions

# Create your views here.
class CarouselListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer


class CarouselDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer