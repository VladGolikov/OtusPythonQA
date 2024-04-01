import pytest
import requests
from api_testing.dog_api.schemas import schema
from jsonschema import validate
from pydantic import BaseModel


class DogRandom(BaseModel):
    message: str
    status: str


def test_list_all_breeds(api_client):
    response = api_client.get_list_all_breeds()
    json_response = response.json()
    assert response.ok, f'status code must be < 400'
    validate(instance=json_response, schema=schema), 'Json structure must be valid'
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
    #print(json_response)
    # a = [DogRandom.model_validate(obj) for obj in json_response]
    # print(a)
    print(DogRandom.message)
    # random_dogs = [DogRandom.model_validate(mess) for obj in json_response]
    # for random_dog in random_dogs:
    #     print(random_dog.status)
    #     assert random_dog.status == 'success'
    #
    # assert response.ok, f'status code must be < 400'

