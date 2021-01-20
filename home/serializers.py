from rest_framework import serializers
from .models import HomePageContent
from artwork.models import Artwork
from versatileimagefield.serializers import VersatileImageFieldSerializer


class InchSerializer (serializers.Serializer):

    def to_representation(self, instance):
        return "{}\"".format(instance)


class ArtworkSerializer(serializers.ModelSerializer):
    artimage = VersatileImageFieldSerializer(
        sizes='carousel_gallery'
    )
    media = serializers.CharField(source='get_media_display')
    height = InchSerializer()
    width = InchSerializer()

    class Meta:
        model = Artwork
        fields = ('id', 'title', 'media', 'artimage', 'width', 'height')


class HomePageSerializer(serializers.ModelSerializer):
    artwork = ArtworkSerializer(many=False)

    class Meta:
        model = HomePageContent
        fields = ('hometitle', 'artwork', 'bodycontent')
