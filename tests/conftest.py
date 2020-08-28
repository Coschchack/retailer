import logging

import pytest
from rest_framework.test import APIClient


@pytest.fixture(scope="module")
def api_client():
    return APIClient()


@pytest.fixture(scope="module")
def logger(request):
    return logging.getLogger(name=request.module.__name__)
