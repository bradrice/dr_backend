from rest_framework import serializers
from .models import Sketchbook
from versatileimagefield.serializers import VersatileImageFieldSerializer


class SketchbookSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='detail')
    artimage = VersatileImageFieldSerializer(
        sizes='image_gallery'
    )
    media = serializers.CharField(source='get_media_display')

    def format_price(self, instance):
        return "${}".format(instance.price)

    class Meta:
        model = Sketchbook
        fields = ('url', 'id', 'artimage', 'title', 'media', 'description', 'showOnWebsite')

    
class MediaTypeSerializer (serializers.ModelSerializer):

    def to_representation(self, value):
        return {'key': value.media, 'value': value.get_media_display()}

    class Meta:
        model = Sketchbook
        fields = ['media', 'media_display']
