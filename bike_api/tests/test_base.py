import requests
import random
import time


class TestBAse:

    def test_user_register(self, users_register):
        response = requests.post(users_register, data={
            "username": "ivan",
            "password": "qwerty",
            "email": "ivan@example.com"
        })
        assert response.status_code == 201
