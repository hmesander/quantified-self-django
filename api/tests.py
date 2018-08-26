import json
from api.models import Food
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase

class FoodViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.banana = Food.objects.create(name="banana", calories=80)
        self.oatmeal = Food.objects.create(name="oatmeal", calories=200)

    def test_status_for_all_foods(self):
        response = self.client.get('/api/v1/foods/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_gets_all_foods(self):
        response = self.client.get('/api/v1/foods/')
        result = self.client.get('/api/v1/foods/').json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["name"], self.banana.name)
        self.assertEqual(result[0]["calories"], self.banana.calories)
        self.assertEqual(result[1]["name"], self.oatmeal.name)
        self.assertEqual(result[1]["calories"], self.oatmeal.calories)

    def test_gets_a_single_food(self):
        response = self.client.get('/api/v1/foods/2')
        result = self.client.get('/api/v1/foods/2').json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 3)
        self.assertEqual(result["name"], self.oatmeal.name)
        self.assertEqual(result["calories"], self.oatmeal.calories)
