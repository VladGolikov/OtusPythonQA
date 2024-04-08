import pytest

from api_testing.dog_api.dog_api_client.dog_api_client import DogApiClient


@pytest.fixture(scope="function")
def api_client():
    client = DogApiClient()
    return client


# @pytest.fixture()
# def data_wrapper_dogs():
#     """fixtures for perimeters of figures"""
#
#     def _wrapper(data: str):
#
#
#     yield _wrapper

@pytest.fixture()
def number():
    number = [x for x in range(1, 51)]
    yield number
