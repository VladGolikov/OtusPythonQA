import pytest

from api_testing.brewery_api.brewery_api_client.brewery_api_client import BreweryApiClient


@pytest.fixture(scope="function")
def api_client():
    client = BreweryApiClient()
    return client


@pytest.fixture()
def schema_by_country():
    return {
        "type": "object",
        "properties": {
            "total": {"type": "string"},
            "page": {"type": "string"},
            "per_page": {"type": "string"}

        },
        "required": ["total", "page", 'per_page']}


@pytest.fixture()
def schema_pagination():
    return {
        "type": "array",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "brewery_type": {"type": "string"},
            "address_1": {"type": "string"},
            "city": {"type": "string"},
            "state_province": {"type": "string"},
            "postal_code": {"type": "string"},
            "country": {"type": "string"},
            "longitude": {"type": "string"},
            "latitude": {"type": "string"},
            "phone": {"type": "string"},
            "website_url": {"type": "string"},
            "state": {"type": "string"},
            "street": {"type": "string"}
        },
        "required": ["id", "name", "brewery_type", "address_1", "city", "state_province", "postal_code", "country",\
                     "longitude", "latitude", "phone", "website_url", "state", "street"]}
