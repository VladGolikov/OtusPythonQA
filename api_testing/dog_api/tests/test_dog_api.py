import pytest
import requests
from api_testing.dog_api.schemas import schema_all_breeds, schema_random_image
from jsonschema import validate
from pydantic import BaseModel


# class DogRandom(BaseModel):
#     message: str
#     status: str


def test_list_all_breeds(api_client):
    response = api_client.get_list_all_breeds()
    json_response = response.json()
    assert response.ok, f'status code must be < 400'
    validate(instance=json_response, schema=schema_all_breeds), 'Json structure must be valid'
    for dog in json_response['message']:
        assert type(dog) == str, 'breed must be string'
    for subbreed in json_response['message'].values():
        assert type(subbreed) == list, 'subbreeds must be stored in lists'
        if subbreed:
            for item in subbreed:
                assert type(item) == str, 'subbreed must be string'


def test_single_random_image(api_client):
    response = api_client.get_single_random_image()
    json_response = response.json()
    assert response.ok, f'status code must be < 400'
    validate(instance=json_response, schema=schema_random_image), 'Json structure must be valid'
    assert json_response['message'].split('.')[-1] == 'jpg', 'Image should be jpg'
    assert json_response['status'] == 'success'


@pytest.mark.parametrize("number_of_dogs", [x for x in range(1, 51)])
def test_multiple_random_image(api_client, number_of_dogs):
    response = api_client.get_mulpiple_random_images(number_of_dogs)
    json_response = response.json()
    # print(len((json_response['message'])))
    assert json_response

