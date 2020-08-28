import pytest

from api.models import Product


@pytest.fixture()
def created_product():
    return Product.objects.create(name="product1", price=10, description="my awesome description!")
