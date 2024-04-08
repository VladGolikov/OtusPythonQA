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


    # def get_miltiple_random_images(self):
    #
    #     number_of_dogs = [dog for dog in range(1, 51)]
    #     # for dog in number_of_dogs:
    #     response = self.session.get(url=f'{self.base_url}/breeds/image/random/{dog}')
    #     return response

    def get_mulpiple_random_images(self, number_of_dogs):
        # number_of_dogs = [x for x in range(1,51)]
        response = self.session.get(url=f'{self.base_url}/breeds/image/random/{number_of_dogs}')
        return response



