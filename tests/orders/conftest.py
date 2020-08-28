import pytest

from api.models import Product, Order


@pytest.fixture()
def created_product():
    return Product.objects.create(name="product1", price=10.45)


@pytest.fixture()
def created_order(created_product):
    order = Order.objects.create()
    order.products.add(created_product)
    return order
