from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, PrimaryKeyRelatedField

from api.models import Product, Order


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'created_at')


class OrderSerializer(ModelSerializer):
    """
    General serializer for Orders. 'products' contains only product primary keys, to limit the size of the response.
    """
    class Meta:
        model = Order
        fields = ('id', 'products', 'created_at')


class OrderDetailsSerializer(ModelSerializer):
    """
    Serializer for Order details. 'products' contains full information about each of the product like name or id.
    """
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'products', 'created_at')


class OrderHyperlinkSerializer(HyperlinkedModelSerializer):
    """
    Serializer that includes hyperlinks to Order details.
    """
    products = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'products', 'created_at', 'url')
