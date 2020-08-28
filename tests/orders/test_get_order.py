import pytest
from rest_framework import status

from tests.api_urls import ApiUrls


pytestmark = pytest.mark.django_db


@pytest.fixture()
def order_get_response(api_client, created_order):
    response = api_client.get(ApiUrls.get_order_detail_url(created_order.id))
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, dict)
    return response.data


def test_get_response_id(order_get_response):
    order_id = order_get_response["id"]
    assert isinstance(order_id, int)
    assert order_id == 1


def test_get_response_created_at(order_get_response):
    assert isinstance(order_get_response["created_at"], str)


def test_get_response_products(order_get_response, created_product):
    assert isinstance(order_get_response["products"], list)
    assert len(order_get_response["products"]) == 1
    response_product = order_get_response["products"][0]
    assert response_product["id"] == created_product.id
    assert response_product["name"] == created_product.name
    assert response_product["price"] == str(created_product.price)
    assert response_product["description"] == created_product.description
