import pytest


@pytest.fixture
def base_url():
    return 'http://django:8000'


@pytest.fixture
def api(base_url):
    return base_url + '/api'


@pytest.fixture
def users(api):
    return api + '/users'


@pytest.fixture
def users_register(users):
    return users + '/register'
