from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from api.models import Product, Order, ProductFeature
from api.serializers import ProductSerializer, OrderSerializer, OrderDetailsSerializer, OrderHyperlinkSerializer, OrderCreateSerializer, OS

# Create your views here.


class ProductViewSet(ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_by_action = {
        "retrieve": OrderDetailsSerializer,
        "list": OS,
        "create": OrderCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_by_action.get(self.action, OrderSerializer)
