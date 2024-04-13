import pytest

from api_testing.dog_api.dog_api_client.dog_api_client import DogApiClient


@pytest.fixture(scope="function")
def api_client():
    client = DogApiClient()
    return client


@pytest.fixture()
def data_wrapper_breeds():
    """fixture for areas of figures"""

    def _wrapper(data: str):
        if data == 'cute_dogs':
            return ["akita", "hound"]
        if data == 'dangerous_dogs':
            return ['boxer']
        if data == 'list_subbreeds':
            return ['hound']

    yield _wrapper


@pytest.fixture()
def schema_all_breeds():
    return {
        "type": "object",
        "properties": {
            "message": {"type": "object"},
            'status': {"type": "string"}
        },
        "required": ["message", "status"]}


@pytest.fixture()
def schema_random_image():
    return {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            'status': {"type": "string"}
        },
        "required": ["message", "status"]}


@pytest.fixture()
def schema_multiple_random_image():
    return {
        "type": "object",
        "properties": {
            "message": {"type": "array"},
            'status': {"type": "string"}
        },
        "required": ["message", "status"]}


@pytest.fixture()
def schema_hound_list():
    return {
        "type": "object",
        "properties": {
            "message": {"type": "array",
                        'items': {'type': 'string',
                                  'enum':
                                      ["afghan",
                                       "basset",
                                       "blood",
                                       "english",
                                       "ibizan",
                                       "plott",
                                       "walker"]}},
            'status': {"type": "string"}},
        "required": ["message", "status"]}
