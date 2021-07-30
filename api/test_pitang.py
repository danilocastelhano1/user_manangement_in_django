from rest_framework.test import APITestCase

# Create your tests here.

DATA_BODY = {
    "first_name": "Jon",
    "last_name": "Doe",
    "email": "jon@doe.com",
    "password": "123456",
    "phones": [
        {
            "number": 999998888,
            "area_code": 11,
            "country_code": "+55"
        }
    ]
}


class AccountTests(APITestCase):
    def test_me_without_login(self):
        resp = self.client.get('/api/me/')
        assert resp.status_code == 401

    def test_me_with_login(self):
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.get_token())
        resp = self.client.get('/api/me/')
        assert resp.status_code == 200

    def test_signup(self):
        resp = self.client.post('/api/signup/', DATA_BODY, format='json')
        assert resp.status_code == 201

    def test_signin(self):
        self.test_signup()

        data = {
            "email": "jon@doe.com",
            "password": "123456"
        }
        resp = self.client.post('/api/signin/', data, format='json')
        assert resp.status_code == 200

    def get_token(self):
        resp = self.client.post('/api/signup/', DATA_BODY, format='json')
        return resp.json()['token']
