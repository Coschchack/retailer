import pytest
from rest_framework import status

from tests.api_urls import ApiUrls


pytestmark = pytest.mark.django_db


@pytest.fixture()
def retrieved_product_list(api_client):
    response = api_client.get(ApiUrls.get_product_list_url())
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
    return response.data


@pytest.fixture()
def product_from_list(retrieved_product_list):
    assert len(retrieved_product_list) == 1
    return retrieved_product_list[0]


def test_product_id(created_product, product_from_list):
    product_id = product_from_list["id"]
    assert isinstance(product_id, int)
    assert product_id == created_product.id


def test_product_name(created_product, product_from_list):
    product_name = product_from_list["name"]
    assert isinstance(product_name, str)
    assert product_name == created_product.name


def test_product_description(created_product, product_from_list):
    product_description = product_from_list["description"]
    assert isinstance(product_description, str)
    assert product_description == created_product.description


def test_product_price(created_product, product_from_list):
    product_price = product_from_list["price"]
    assert isinstance(product_price, str)
    assert product_price == f"{created_product.price}.00"


@pytest.mark.usefixtures("created_product")
def test_product_created_at(product_from_list):
    product_created_at = product_from_list["created_at"]
    assert isinstance(product_created_at, str)
