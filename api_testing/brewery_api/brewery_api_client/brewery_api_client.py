import requests


class BreweryApiClient:
    def __init__(self, base_ulr='https://api.openbrewerydb.org/v1/breweries'):
        self.session = requests.Session()
        self.base_url = base_ulr

    def get_list_all_breeds(self, country):
        response = self.session.get(url=f'{self.base_url}/meta?by_country={country}')
        return response

    def pagination(self, city, per_page):
        response = self.session.get(url=f'{self.base_url}/?by_city={city}&per_page={per_page}')
        return response

    def type(self, type, per_page):
        response = self.session.get(url=f'{self.base_url}/?by_type={type}&per_page={per_page}')
        return response

    def postal(self, postal, per_page):
        response = self.session.get(url=f'{self.base_url}/?by_postal={postal}&per_page={per_page}')
        return response

    def sort_by(self, state, sort_by, per_page):
        response = self.session.get(url=f'{self.base_url}/?by_state={state}&sort=type,name:{sort_by}&per_page={per_page}')
        return response

