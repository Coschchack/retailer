import pytest
from rest_framework import status

from tests.api_urls import ApiUrls


pytestmark = pytest.mark.django_db


def step_get_orders_list(api_client):
    orders_list_response = api_client.get(ApiUrls.get_order_list_url())
    assert orders_list_response.status_code == status.HTTP_200_OK
    return orders_list_response.data


def test_simple_order_delete(api_client, created_order):
    response = api_client.delete(ApiUrls.get_order_detail_url(created_order.id))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.data is None


def test_delete_order_and_compare_with_orders_list(api_client, created_order):
    assert created_order.id in [order["id"] for order in step_get_orders_list(api_client)]
    order_del_response = api_client.delete(ApiUrls.get_order_detail_url(created_order.id))
    assert order_del_response.status_code == status.HTTP_204_NO_CONTENT
    assert created_order.id not in [order["id"] for order in step_get_orders_list(api_client)]
