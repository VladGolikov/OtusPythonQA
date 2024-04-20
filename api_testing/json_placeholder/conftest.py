import pytest

from api_testing.json_placeholder.json_api_client.json_api_client import JSONApiClient


@pytest.fixture(scope="function")
def api_client():
    client = JSONApiClient()
    return client


@pytest.fixture()
def schema_posts():
    return {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "body": {"type": "string"},
            "userId": {"type": "number"},
            "id": {"type": "number"}
        },
        "required": ["title", "body", "userId", "id"]}

@pytest.fixture()
def schema_users_posts():
    return {
        "type": "array",
        "properties": {
            "title": {"type": "string"},
            "body": {"type": "string"},
            "userId": {"type": "number"},
            "id": {"type": "number"}
        },
        "required": ["title", "body", "userId", "id"]}

@pytest.fixture()
def schema_put():
    return {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "body": {"type": "string"},
            "id": {"type": "number"}
        },
        "required": ["title", "body", "id"]}
