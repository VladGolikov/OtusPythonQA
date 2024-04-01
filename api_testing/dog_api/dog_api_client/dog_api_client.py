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
