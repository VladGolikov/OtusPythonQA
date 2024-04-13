import pytest
from jsonschema import validate


def test_list_all_breeds(api_client, schema_all_breeds):
    response = api_client.get_list_all_breeds()
    json_response = response.json()
    assert response.ok, 'status code must be < 400'
    validate(instance=json_response, schema=schema_all_breeds), 'Json structure must be valid'
    for dog in json_response['message']:
        assert type(dog) == str, 'breed must be string'
    for subbreed in json_response['message'].values():
        assert type(subbreed) == list, 'subbreeds must be stored in lists'
        if subbreed:
            for item in subbreed:
                assert type(item) == str, 'subbreed must be string'


def test_single_random_image(api_client, schema_random_image):
    response = api_client.get_single_random_image()
    json_response = response.json()
    assert response.ok, 'status code must be < 400'
    validate(instance=json_response, schema=schema_random_image), 'Json structure must be valid'
    assert json_response['message'].split('.')[-1] == 'jpg', 'Image should be jpg'
    assert json_response['status'] == 'success', 'Status in JSON must be "success"'


@pytest.mark.parametrize("number_of_dogs", [x for x in range(1, 51)])
def test_multiple_random_image(api_client, number_of_dogs, schema_multiple_random_image):
    response = api_client.get_mulpiple_random_images(number_of_dogs)
    json_response = response.json()
    assert response.ok, 'status code must be < 400'
    validate(instance=json_response, schema=schema_multiple_random_image), 'Json structure must be valid'
    assert json_response['status'] == 'success', 'Status in JSON must be "success"'
    all_jpeg = all('jpg' in item for item in json_response['message'])
    assert all_jpeg, 'all images must be in jpg'


@pytest.mark.parametrize("breeds", ['cute_dogs', 'dangerous_dogs'])
def test_random_image_breed_collection(api_client, data_wrapper_breeds, breeds, schema_random_image):
    breed = data_wrapper_breeds(data=breeds)
    for item in breed:
        response = api_client.get_random_image_from_collection(item)
        assert response.ok, 'status code must be < 400'
        json_response = response.json()
        validate(instance=json_response, schema=schema_random_image), 'Json structure must be valid'
        assert json_response['status'] == 'success'
        assert json_response['message'].split('.')[-1] == 'jpg'


def test_list_all_subbreeds(api_client, schema_hound_list):
    response = api_client.get_list_all_sub_breeds()
    assert response.ok
    json_response = response.json()
    validate(instance=json_response, schema=schema_hound_list), 'Json structure must be valid'
    assert json_response['status'] == 'success'
