import pytest
import requests


class DogApiClient:
    def __init__(self, base_ulr='https://dog.ceo/api'):
        self.session = requests.Session()
        self.base_url = base_ulr

    def get_list_all_breeds(self):
        response = self.session.get(url=f'{self.base_url}/breeds/list/all')
        return response

    def get_single_random_image(self):
        response = self.session.get(url=f'{self.base_url}/breeds/image/random')
        return response

    def get_mulpiple_random_images(self, number_of_dogs):
        response = self.session.get(url=f'{self.base_url}/breeds/image/random/{number_of_dogs}')
        return response

    def get_random_image_from_collection(self, breed):
        response = self.session.get(url=f'{self.base_url}/breed/{breed}/images/random')
        return response

    def get_list_all_sub_breeds(self):
        response = self.session.get(url=f'{self.base_url}/breed/hound/list')
        return response
