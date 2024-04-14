import requests


class JSONApiClient:
    def __init__(self, base_ulr='https://jsonplaceholder.typicode.com'):
        self.session = requests.Session()
        self.base_url = base_ulr

    def post(self, body):
        response = self.session.post(url=f'{self.base_url}/posts', json=body)
        return response

    def get_all_users_posts(self, user_id):
        response = self.session.get(url=f'{self.base_url}/posts?userId={user_id}')
        return response

    def get_different_info(self, route_1, id, route_2):
        response = self.session.get(url=f'{self.base_url}/{route_1}/{id}/{route_2}')
        return response

    def delete(self, route_1, id):
        response = self.session.delete(url=f'{self.base_url}/{route_1}/{id}')
        return response

    def put(self, user_id, body):
        response = self.session.put(url=f'{self.base_url}/posts/{user_id}', json=body)
        return response
