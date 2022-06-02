import json

from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ValidateDataTest(APITestCase):

    def test_registration_with_valid_data(self):
        data = {
            "username": "user1db",
            "password": "definiton100",
            "password2": "definiton100"
        }
        response = self.client.post(reverse('sign-up'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_registration_with_diff_pass(self):
        data = {
            "username": "user",
            "password": "definiton100",
            "password1": "definiton101"
        }
        response = self.client.post(reverse('sign-up'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_registration_with_empty_field(self):
        data = {
            "username": "",
            "password": "",
            "password1": ""
        }
        response = self.client.post(reverse('sign-up'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

