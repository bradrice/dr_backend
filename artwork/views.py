from django.shortcuts import render
from django.http import JsonResponse 

from .models import Artwork
from .serializers import ArtworkSerializer, MediaTypeSerializer
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
        'artworks': reverse('artworks', request=request, format=format),
        'carousels': reverse('carousels', request=request, format=format)
    })

# Create your views here.
class ArtworkListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ArtworkSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        return Artwork.objects.filter(showOnWebsite=True)

class ArtworkFullListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ArtworkSerializer
    def get_queryset(self):
        return Artwork.objects.filter(showOnWebsite=True)


class ArtworkDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ArtworkSerializer
    queryset = Artwork.objects.all()


class ArworkIsSold(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ArtworkSerializer
    queryset = Artwork.objects.all()

    def partial_update(self, request, pk=None):
        data = {"sold":True,"forSale":False}
        serializer = ArtworkSerializer(context={'request': request},data=data, partial=True)
        serializer.is_valid()
        serializer.save()
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    

class ArtworkMediaList(generics.ListAPIView):
    serializer_class = ArtworkSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """
        Optionally restricts the returned artwork to the media query params
        """
        queryset = Artwork.objects.all()
        # queryset = queryset.filter(media='W')
        # return queryset
        mediaparam = self.request.query_params.get('media', None)
        if mediaparam is not None:
            if mediaparam != 'all':
                queryset = queryset.filter(media=mediaparam)
            else:
                queryset = Artwork.objects.all()
        return queryset


class ArtworkMediaTypes(generics.ListAPIView):
    serializer_class = MediaTypeSerializer

    def get_queryset(self):
        """
        Get unique media types from objects
        """
        mediaitems = Artwork.objects.all().order_by('media').distinct('media')
        # items = set(elements)
        print (d)
        return mediaitems

    