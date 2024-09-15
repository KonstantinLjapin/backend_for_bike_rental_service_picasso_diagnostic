import requests
import json


def get_token(url):
    url_user_token_jwt = url + '/token/'
    payload = {"username": "ivan",
               "password": "qwerty"}
    response_t = requests.post(url_user_token_jwt, data=payload)
    temp_user_jwt = response_t.json().get("access")
    token = 'Bearer ' + temp_user_jwt
    return token


class TestBAse:
    temp_jwt = str('')

    def test_user_register(self, users_register):
        response = requests.post(users_register, data={
            "username": "ivan",
            "password": "qwerty",
            "email": "ivan@example.com"
        })
        assert response.status_code == 201

    def test_user_login(self, users_login):
        response = requests.post(users_login, data={
            "username": "ivan",
            "password": "qwerty"
        })
        assert response.status_code == 200

    def test_users_get_jwt(self, api):
        url_user_token_jwt = api + '/token/'
        payload = {"username": "ivan",
                   "password": "qwerty"}
        response = requests.post(url_user_token_jwt, data=payload)
        self.temp_jwt += response.json().get("access")
        assert isinstance(self.temp_jwt, str)

    def test_users_profile(self, api, users_profile):
        token = get_token(api)
        response = requests.get(users_profile, headers={'Authorization': token})
        assert response.status_code == 200

    def test_bike_list(self, api, bike_list):
        token = get_token(api)
        response = requests.get(bike_list, headers={'Authorization': token})
        assert response.status_code == 200

    def test_rent_start(self, api, rent_start):
        token = get_token(api)
        payload = {
            "id": 1,
            "bike_model": "mountain_bike_dragon",
            "fuse": True
        }
        response = requests.put(rent_start, data=payload, headers={'Authorization': token})
        assert response.status_code == 202

    def test_rent_end(self, api, rent_end):
        token = get_token(api)
        payload = {
            "id": 1,
            "bike_model": "mountain_bike_dragon",
            "fuse": True
        }
        response = requests.put(rent_end, data=payload, headers={'Authorization': token})
        assert response.status_code == 205

    def test_users_logout(self, api, users_logout):
        url_user_token_jwt = api + '/token/'
        payload = {"username": "ivan",
                   "password": "qwerty"}
        response_t = requests.post(url_user_token_jwt, data=payload)
        temp_user_jwt = response_t.json().get("access")
        token = 'Bearer ' + temp_user_jwt
        response = requests.post(users_logout, data={
            "username": "ivan",
            "password": "qwerty"

        }, headers={'Authorization': token})
        assert response.status_code == 200
