from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.response import Response
from django.urls import reverse
import json
from . import models
from typing import *


# Create your tests here.


class UserAccount(APITestCase):

    def test_create_user(self):
        url: str = reverse('user_list_api')
        data: Dict[str: Any] = {
            "first_name": "Calebe",
            "last_name": "Bianchinni",
            "cbj_id": 10,
            "primary_phone": 991919191,
            "email": "teste2@teste.com",
            "notes": "olar",
            "alternative_phone": 9191828191,
            "cpf": 9189281829,
            "rg": 981298129182,
        }
        response: Response = self.client.post(path=url,
                                              data=data,
                                              format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.User.objects.get().id,
                         response.data['id'])
