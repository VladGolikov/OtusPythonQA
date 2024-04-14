import pytest
from jsonschema import validate


@pytest.mark.parametrize("json", [{"title": "foo", "body": "bar", "userId": 1},
                                  {"title": "test", "body": "restaurant", "userId": 2}])
def test_post(api_client, json, schema_posts):
    response = api_client.post(json)
    assert response.status_code == 201, "status code must be 201"
    json_response = response.json()
    assert json_response['userId'] == json['userId'], "User in json response must be the same as in body"
    validate(instance=json_response, schema=schema_posts), "Json structure must be valid"


@pytest.mark.parametrize("user", [user for user in range(1, 11)])
def test_all_user_posts(api_client, user, schema_users_posts):
    response = api_client.get_all_users_posts(user)
    assert response.status_code == 200, "status code must be 200"
    json_response = response.json()
    assert len(json_response) == 10, "all users have only 10 posts"
    validate(instance=json_response, schema=schema_users_posts), "Json structure must be valid"


@pytest.mark.parametrize("route_2", ["comments", "photos", "albums", "todos", "posts"])
@pytest.mark.parametrize("id", [1])
@pytest.mark.parametrize("route_1", ["posts", "albums", "users"])
def test_different_info(api_client, route_1, id, route_2):
    response = api_client.get_different_info(route_1, id, route_2)
    assert response.status_code == 200, "status code must be 200"
    assert response.json(), "response must have json response"


@pytest.mark.parametrize("id", [1, 10])
@pytest.mark.parametrize("route_1", ["posts", "albums", "users"])
def test_delete(api_client, route_1, id):
    response = api_client.delete(route_1, id)
    assert response.status_code == 200, "status code must be 200"


@pytest.mark.parametrize("user", [1, 5])
@pytest.mark.parametrize("json", [{"title": "flor", "body": "bark"},
                                  {"title": "candle", "body": "uranium"}])
def test_post(api_client, user, json, schema_put):
    response = api_client.put(user, json)
    assert response.status_code == 200, "status code must be 200"
    json_response = response.json()
    assert json_response['id'] == user, "User in json response must be the same as in query"
    validate(instance=json_response, schema=schema_put), "Json structure must be valid"
