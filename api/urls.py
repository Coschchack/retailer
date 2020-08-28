from django.urls import include, path
from rest_framework import routers

from api.views import OrderViewSet, ProductViewSet


router = routers.DefaultRouter()
router.register(r'api/products', ProductViewSet, basename='product')
router.register(r'api/orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
