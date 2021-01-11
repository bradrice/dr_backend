from rest_framework import serializers
from .models import Carousel
from artwork.models import Artwork
from versatileimagefield.serializers import VersatileImageFieldSerializer

class ArtworkSerializer(serializers.ModelSerializer):
    artimage = VersatileImageFieldSerializer(
        sizes='carousel_gallery'
    )
    class Meta:
        model = Artwork
        fields = ('id', 'title', 'media', 'artimage')


class CarouselSerializer(serializers.ModelSerializer):
    artwork = ArtworkSerializer(many=True)

    class Meta:
        model = Carousel
        fields = ('id', 'carouseltitle', 'artwork')


