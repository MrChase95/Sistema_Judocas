from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.response import Response
from django.urls import reverse
import json
from . import models
from typing import *


# Create your tests here.


class UserAccount(APITestCase):
    url: str = reverse('user_list_api')
    init_data = {
        "first_name": "Calebe",
        "last_name": "Bianchinni",
        "username": "pythonLover",
        "password": "pythonLover",
        "cbj_id": 10,
        "primary_phone": 991919191,
        "email": "teste2@teste.com",
        "notes": "olar",
        "alternative_phone": 9191828191,
        "cpf": 35334719857,
        "rg": 9812981291,
    }

    def test_create_user(self):
        response: Response = self.client.post(path=self.url,
                                              data=self.init_data,
                                              format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg='User not Created')
        self.assertEqual(models.User.objects.get().id,
                         response.data['id'],
                         msg='IDs not matched')

    def test_cpf(self):
        alter_data = self.init_data.copy()
        alter_data['cpf'] = 35334719875
        response: Response = self.client.post(path=self.url,
                                              data=alter_data,
                                              format='json')
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED,
                            msg='User Created')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST,
                         msg='CPF Validation Failed')

    def test_email_is_unique(self):
        response: Response = self.client.post(path=self.url,
                                              data=self.init_data,
                                              format='json')
        alter_data = self.init_data.copy()
        alter_data['username'] = 'CLover'
        response2: Response = self.client.post(path=self.url,
                                               data=alter_data,
                                               format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                            msg='User Created')
        self.assertNotEqual(response2.status_code, status.HTTP_201_CREATED,
                            msg='User Created')

    def test_username_is_unique(self):
        response: Response = self.client.post(path=self.url,
                                              data=self.init_data,
                                              format='json')
        alter_data = self.init_data.copy()
        alter_data['email'] = 'teste@teste.com'
        response2: Response = self.client.post(path=self.url,
                                               data=alter_data,
                                               format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED,
                         msg='User Created')
        self.assertNotEqual(response2.status_code, status.HTTP_201_CREATED,
                            msg='User Created')
