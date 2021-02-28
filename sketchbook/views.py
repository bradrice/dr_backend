from django.shortcuts import render
from django.http import JsonResponse 

from .models import Sketchbook
from .serializers import SketchbookSerializer, MediaTypeSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 30

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Sketchbooks': reverse('Sketchbooks', request=request, format=format),
    })

# Create your views here.
class SketchbookListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SketchbookSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        return Sketchbook.objects.filter(showOnWebsite=True)

class SketchbookFullListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SketchbookSerializer
    def get_queryset(self):
        return Sketchbook.objects.filter(showOnWebsite=True)


class SketchbookDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SketchbookSerializer
    queryset = Sketchbook.objects.all()
    

class SketchbookMediaList(generics.ListAPIView):
    serializer_class = SketchbookSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """
        Optionally restricts the returned Sketchbook to the media query params
        """
        queryset = Sketchbook.objects.all()
        # queryset = queryset.filter(media='W')
        # return queryset
        mediaparam = self.request.query_params.get('media', None)
        if mediaparam is not None:
            if mediaparam != 'all':
                queryset = queryset.filter(media=mediaparam, showOnWebsite=True)
            else:
                queryset = Sketchbook.objects.filter(showOnWebsite=True)
        return queryset


class SketchbookMediaTypes(generics.ListAPIView):
    serializer_class = MediaTypeSerializer

    def get_queryset(self):
        """
        Get unique media types from objects
        """
        mediaitems = Sketchbook.objects.filter(showOnWebsite=True).order_by('media').distinct('media')
        # items = set(elements)
        return mediaitems

    