from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, PrimaryKeyRelatedField, IntegerField, DateTimeField

from api.models import Product, Order, ProductFeature


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


class OrderCreateSerializer(ModelSerializer):
    product_id = IntegerField(source="product.id")

    class Meta:
        model = ProductFeature
        fields = ('product_id', 'size')

    def create(self, validated_data):
        # profile_data = validated_data.pop('profile')
        # user = User.objects.create(**validated_data)
        # Profile.objects.create(user=user, **profile_data)

        # To add more products (products features) to an order:
        # 1. Create an order
        # 2. Create PF -> ProductFeature.objects.create(order=pf_order, product=Product.objects.get(id=1), size="S")
        # 3. Create another PF with the same order-> ProductFeature.objects.create(order=pf_order, product=Product.objects.get(id=2), size="M")
        # 4. Get order products: Order.objects.get(id=id_of_pf_order).products.all() -> it will return 2 products


        p = Product.objects.get(id=3)
        o = Order.objects.create()
        o.products.add(p)

        return ProductFeature(order=o, product=p, size="L")


class OS(ModelSerializer):
    # order = OrderSerializer()
    # created_at = DateTimeField(source="order.created_at")

    class Meta:
        model = ProductFeature
        fields = ('id', 'order', 'product', 'size')



# class UserSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'profile']
#
#     def create(self, validated_data):
#         profile_data = validated_data.pop('profile')
#         user = User.objects.create(**validated_data)
#         Profile.objects.create(user=user, **profile_data)
#         return user