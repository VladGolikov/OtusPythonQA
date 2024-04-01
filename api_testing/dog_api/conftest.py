import pytest

from api_testing.dog_api.dog_api_client.dog_api_client import DogApiClient


@pytest.fixture(scope="function")
def api_client():
    client = DogApiClient()
    return client


