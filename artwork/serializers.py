from rest_framework import serializers
from .models import Artwork
from versatileimagefield.serializers import VersatileImageFieldSerializer

class PriceSerializer (serializers.DecimalField):
    fields = ('price',)

    def to_representation(self, instance):
        return "${}".format(instance)

class InchSerializer (serializers.Serializer):

    def to_representation(self, instance):
        return "{}\"".format(instance)

class ArtworkSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='detail')
    artimage = VersatileImageFieldSerializer(
        sizes='image_gallery'
    )
    price_format = serializers.SerializerMethodField('format_price')
    media = serializers.CharField(source='get_media_display')
    height = InchSerializer()
    width = InchSerializer()

    def format_price(self, instance):
        return "${}".format(instance.price)

    class Meta:
        model = Artwork
        fields = ('url', 'id', 'title', 'media', 'description', 'created', 'width', 'height', 'artimage', 'sold', 'price', 'price_format', 'forSale', 'showOnWebsite')