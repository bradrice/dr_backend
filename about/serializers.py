from rest_framework import serializers
from .models import AboutPageContent
from artwork.models import Artwork
from versatileimagefield.serializers import VersatileImageFieldSerializer

class ArtworkSerializer(serializers.ModelSerializer):
    artimage = VersatileImageFieldSerializer(
        sizes='carousel_gallery'
    )
    class Meta:
        model = Artwork
        fields = ('id', 'title', 'media', 'artimage')


class AboutPageSerializer(serializers.ModelSerializer):
    artwork = ArtworkSerializer(many=False)

    class Meta:
        model = AboutPageContent
        fields = ('id', 'abouttitle', 'artwork', 'bodycontent')


