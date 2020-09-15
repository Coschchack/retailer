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


class OrderSerializer(HyperlinkedModelSerializer):
    detailed_products = DetailedProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'url', 'detailed_products', 'created_at')

    def create(self, validated_data):
        passed_detailed_products = validated_data.get('detailed_products')
        self._raise_exception_on_empty_products(passed_detailed_products)
        new_order = Order.objects.create()
        for details in passed_detailed_products:
            self._create_detailed_product(new_order, details)
        return new_order

    def update(self, instance, validated_data):
        passed_detailed_products = validated_data.get('detailed_products')
        self._raise_exception_on_empty_products(passed_detailed_products)
        for existing_product_details in instance.detailed_products.all():
            existing_product_details.delete()
        for product_details in passed_detailed_products:
            self._create_detailed_product(instance, product_details)
        instance.save()
        return instance

    def _create_detailed_product(self, target_order, product_details):
        DetailedProduct.objects.create(
            order=target_order, product=product_details["product"], size=product_details["size"],
            quantity=product_details["quantity"])

    def _raise_exception_on_empty_products(self, products):
        if not products:
            raise EmptyProducts
