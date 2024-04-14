import pytest
from jsonschema import validate


@pytest.mark.parametrize("countries", ["france", "singapore", "south_korea"])
def test_get_brewery_by_country(countries, api_client, schema_by_country):
    response = api_client.get_list_all_breeds(countries)
    assert response.ok, "status code must be < 400"
    json_response = response.json()
    validate(instance=json_response, schema=schema_by_country), "Json structure must be valid"


@pytest.mark.parametrize("city", ["san_diego", "Petaluma"])
@pytest.mark.parametrize("per_page", [1, 2])
def test_pagination_city(city, per_page, api_client, schema_pagination):
    response = api_client.pagination(city, per_page)
    assert response.ok, "status code must be < 400"
    json_response = response.json()
    validate(instance=json_response, schema=schema_pagination), "Json structure must be valid"


@pytest.mark.parametrize("type", ["micro", "nano", "closed"])
@pytest.mark.parametrize("per_page", [1, 2])
def test_type(type, per_page, api_client, schema_pagination):
    response = api_client.pagination(type, per_page)
    assert response.ok, "status code must be < 400"
    json_response = response.json()
    validate(instance=json_response, schema=schema_pagination), "Json structure must be valid"


@pytest.mark.parametrize("postal", ["92101-6618", "92101-1725"])
@pytest.mark.parametrize("per_page", [1, 2])
def test_postal(postal, per_page, api_client, schema_pagination):
    response = api_client.postal(postal, per_page)
    assert response.ok, "status code must be < 400"
    json_response = response.json()
    validate(instance=json_response, schema=schema_pagination), "Json structure must be valid"


@pytest.mark.parametrize("state", ["california", "nevada"])
@pytest.mark.parametrize("sort_by", ["asc", "desc"])
@pytest.mark.parametrize("per_page", [1, 2])
def test_sort_by(state, sort_by, per_page, api_client, schema_pagination):
    response = api_client.sort_by(state, sort_by, per_page)
    assert response.ok, "status code must be < 400"
    json_response = response.json()
    validate(instance=json_response, schema=schema_pagination), "Json structure must be valid"
