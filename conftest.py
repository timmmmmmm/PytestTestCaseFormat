# conftest.py
import pytest


@pytest.fixture
def supply_url():
    return "https://reqres.in/api"


@pytest.fixture
def get_base_url():
    return "https://www.btse.co"
