from rest_framework import serializers
from .models import HomePageContent
from artwork.models import Artwork
from versatileimagefield.serializers import VersatileImageFieldSerializer

class ArtworkSerializer(serializers.ModelSerializer):
    artimage = VersatileImageFieldSerializer(
        sizes='carousel_gallery'
    )
    class Meta:
        model = Artwork
        fields = ('id', 'title', 'media', 'artimage')


class HomePageSerializer(serializers.ModelSerializer):
    artwork = ArtworkSerializer(many=False)

    class Meta:
        model = HomePageContent
        fields = ('hometitle', 'artwork', 'bodycontent')


