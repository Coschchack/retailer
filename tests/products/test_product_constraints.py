import pytest
from django.urls.exceptions import NoReverseMatch
from rest_framework import status

from tests.api_urls import ApiUrls


def test_product_detail_reverse_match():
    with pytest.raises(NoReverseMatch):
        ApiUrls.get_product_detail_url()


@pytest.mark.parametrize("http_request", (
    "GET",
    "PUT",
    "PATCH",
    "DELETE",
))
@pytest.mark.django_db
def test_missing_product_detail_endpoint(api_client, logger, created_product, http_request):
    """
    Based on current requirements, there shouldn't be a product detail API endpoint.
    This test checks if it's not possible to send HTTP methods to such endpoint.
    """
    product_detail_url = f"{ApiUrls.get_product_list_url()}{created_product.id}"
    logger.info(f"Sending {http_request} to {product_detail_url}...")
    response = api_client.generic(method=http_request, path=product_detail_url)
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.parametrize("http_request", (
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
))
def test_other_http_requests_for_product_list(api_client, logger, http_request):
    """
    Based on current requirements, product list should only accept GET requests.
    This test checks if other methods are not allowed.
    """
    product_list_url = ApiUrls.get_product_list_url()
    logger.info(f"Sending {http_request} to {product_list_url}...")
    response = api_client.generic(method=http_request, path=product_list_url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
