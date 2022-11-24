# conftest.py
import pytest


@pytest.fixture
def supply_url():
    return "https://reqres.in/api"


def get_base_url():
    return "https://btse.co"
