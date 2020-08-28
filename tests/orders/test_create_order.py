import pytest
from rest_framework import status

from tests.api_urls import ApiUrls


pytestmark = pytest.mark.django_db


@pytest.fixture()
def order_post_response(api_client, created_product):
    request_data = {
        "products": [
            created_product.id,
        ],
    }
    response = api_client.post(ApiUrls.get_order_list_url(), data=request_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert isinstance(response.data, dict)
    return response.data


def test_post_response_id(order_post_response):
    order_id = order_post_response["id"]
    assert isinstance(order_id, int)
    assert order_id == 1


def test_post_response_created_at(order_post_response):
    assert isinstance(order_post_response["created_at"], str)


def test_post_response_products(order_post_response, created_product):
    response_products = order_post_response["products"]
    assert isinstance(response_products, list)
    assert len(response_products) == 1
    first_product = response_products[0]
    assert isinstance(first_product, int)
    assert first_product == created_product.id
