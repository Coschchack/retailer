import pytest
from rest_framework import status

from api.models import Product
from tests.api_urls import ApiUrls


pytestmark = pytest.mark.django_db


@pytest.fixture()
def new_product():
    return Product.objects.create(name="new_product", price=1.23, description="new product description")


@pytest.fixture()
def order_put_response(api_client, created_order, new_product):
    product_detail_url = ApiUrls.get_order_detail_url(created_order.id)
    request = {
        "products": [
            new_product.id
        ]
    }
    response = api_client.put(product_detail_url, data=request, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, dict)
    return response.data


def test_put_response_id(order_put_response):
    order_id = order_put_response["id"]
    assert isinstance(order_id, int)
    assert order_id == 1


def test_put_response_created_at(order_put_response):
    assert isinstance(order_put_response["created_at"], str)


def test_put_response_products(order_put_response, new_product):
    assert isinstance(order_put_response["products"], list)
    assert len(order_put_response["products"]) == 1
    response_product = order_put_response["products"][0]
    assert isinstance(response_product, int)
    assert response_product == new_product.id
