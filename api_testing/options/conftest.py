import pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--base-url",
                     action="store",
                     default="https://ya.ru",
                     help="This is request url"
                     )

    parser.addoption("--status_code",
                     action="store",
                     default=200,
                     help="This is status_code"
                     )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")


@pytest.fixture
def status_code(request):
    return int(request.config.getoption("--status_code"))


