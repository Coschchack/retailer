from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from api.models import Product, Order, DetailedProduct
from api.exceptions import EmptyProducts


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'created_at')


class DetailedProductSerializer(ModelSerializer):
    class Meta:
        model = DetailedProduct
        fields = ("product", "size", "quantity")


class OrderListSerializer(HyperlinkedModelSerializer):
    detailed_products = DetailedProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'url', 'detailed_products', 'created_at')

    def create(self, validated_data):
        new_order = Order.objects.create()
        passed_detailed_products = validated_data.get('detailed_products')
        if not passed_detailed_products:
            raise EmptyProducts
        for details in passed_detailed_products:
            DetailedProduct.objects.create(
                order=new_order, product=details["product"], size=details["size"], quantity=details["quantity"])
        return new_order

    def update(self, instance, validated_data):
        passed_detailed_products = validated_data.get('detailed_products')
        if not passed_detailed_products:
            raise EmptyProducts
        for existing_product_details in instance.detailed_products.all():
            existing_product_details.delete()
        for product_details in passed_detailed_products:
            DetailedProduct.objects.create(
                order=instance, product=product_details["product"], size=product_details["size"],
                quantity=product_details["quantity"])
        instance.save()
        return instance
