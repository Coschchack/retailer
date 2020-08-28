import pytest
from rest_framework import status

from tests.api_urls import ApiUrls


pytestmark = pytest.mark.django_db


@pytest.fixture()
def retrieved_order_list(api_client):
    response = api_client.get(ApiUrls.get_order_list_url())
    assert response.status_code == status.HTTP_200_OK
    return response.data


@pytest.fixture()
def order_from_list(retrieved_order_list):
    assert len(retrieved_order_list) == 1
    return retrieved_order_list[0]


def test_order_id(created_order, order_from_list):
    order_id = order_from_list["id"]
    assert isinstance(order_id, int)
    assert order_id == created_order.id


@pytest.mark.usefixtures("created_order")
def test_order_products(created_product, order_from_list):
    order_products = order_from_list["products"]
    assert isinstance(order_products, list)
    assert len(order_products) == 1
    assert order_products[0] == created_product.id


@pytest.mark.usefixtures("created_order")
def test_order_created_at(order_from_list):
    order_created_at = order_from_list["created_at"]
    assert isinstance(order_created_at, str)


@pytest.mark.usefixtures("created_order")
def test_order_url(order_from_list):
    order_url = order_from_list["url"]
    assert isinstance(order_url, str)
    assert ApiUrls.get_order_list_url() in order_url
