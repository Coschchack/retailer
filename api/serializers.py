from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from api.models import Product, Order, DetailedProduct


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'created_at')


class DetailedProductSerializer(ModelSerializer):
    class Meta:
        model = DetailedProduct
        fields = ("product", "size")


class OrderListSerializer(HyperlinkedModelSerializer):
    detailed_products = DetailedProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'url', 'detailed_products', 'created_at')

    def create(self, validated_data):
        new_order = Order.objects.create()
        product_details = validated_data.get('detailed_products')
        for details in product_details:
            DetailedProduct.objects.create(
                order=new_order, product=details["product"], size=details["size"])
        return new_order
