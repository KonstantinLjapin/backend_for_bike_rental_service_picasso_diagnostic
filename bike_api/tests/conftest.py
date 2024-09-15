import pytest
import requests

@pytest.fixture
def base_url():
    return 'http://django:8000'


@pytest.fixture
def api(base_url):
    return base_url + '/api'


@pytest.fixture
def bike(api):
    return api + '/bikes'


@pytest.fixture
def bike_list(bike):
    return bike + '/list'


@pytest.fixture
def rent_start(bike):
    return bike + '/rent_start'


@pytest.fixture
def rent_end(bike):
    return bike + '/rent_end'


@pytest.fixture
def users(api):
    return api + '/users'


@pytest.fixture
def users_register(users):
    return users + '/register'


@pytest.fixture
def users_login(users):
    return users + '/login'


@pytest.fixture
def users_profile(users):
    return users + '/profile'


@pytest.fixture
def users_logout(users):
    return users + '/logout'
