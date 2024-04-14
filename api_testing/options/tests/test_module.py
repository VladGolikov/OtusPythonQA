import requests


def test_params(base_url, status_code):
    response = requests.get(base_url)
    assert response.status_code == status_code
