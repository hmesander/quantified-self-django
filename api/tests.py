import json
from api.models import Food, Meal
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase

class WelcomeViewTest(TestCase):
    def test_displays_welcome_page(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>')
        self.assertContains(response, 'Welcome to Quantified Self - Django!')

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

    def test_updates_a_food(self):
        response = self.client.get('/api/v1/foods/2')
        result = self.client.get('/api/v1/foods/2').json()
        self.assertEqual(result["name"], self.oatmeal.name)

        result = self.client.patch('/api/v1/foods/2', {'food': {'name': 'poptart', 'calories': 200}}, format='json').json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["name"], 'poptart')

    def test_creates_a_food(self):
        response = self.client.post('/api/v1/foods/', {'food': {'name': 'lucky charms', 'calories': 180}}, format='json')
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result["id"], 3)
        self.assertEqual(result["name"], 'lucky charms')
        self.assertEqual(result["calories"], 180)

    def test_deletes_a_food(self):
        response = self.client.get('/api/v1/foods/')
        result = response.json()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["name"], self.banana.name)

        self.client.delete('/api/v1/foods/1')

        response = self.client.get('/api/v1/foods/')
        result = response.json()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], self.oatmeal.name)

class MealViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.breakfast = Meal.objects.create(name="Breakfast")
        self.snack = Meal.objects.create(name="Snack")
        self.lunch = Meal.objects.create(name="Lunch")
        self.dinner = Meal.objects.create(name="Dinner")

    def test_gets_all_meals(self):
        response = self.client.get('/api/v1/meals/')
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0]["name"], self.breakfast.name)
        self.assertEqual(result[1]["name"], self.snack.name)
        self.assertEqual(result[2]["name"], self.lunch.name)
        self.assertEqual(result[3]["name"], self.dinner.name)

    def test_gets_a_single_meal(self):
        response = self.client.get('/api/v1/meals/1')
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["name"], self.breakfast.name)

class MealFoodViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.breakfast = Meal.objects.create(name="Breakfast")
        self.snack = Meal.objects.create(name="Snack")
        self.lunch = Meal.objects.create(name="Lunch")
        self.dinner = Meal.objects.create(name="Dinner")
        self.banana = Food.objects.create(name="banana", calories=80)
        self.oatmeal = Food.objects.create(name="oatmeal", calories=200)

    def test_associates_food_with_a_meal(self):
        response = self.client.get('/api/v1/meals/1')
        result = response.json()
        self.assertEqual(result["name"], self.breakfast.name)
        self.assertEqual(result["foods"], [])

        response = self.client.post('/api/v1/meals/1/foods/1')
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result["message"], f"Successfully added {self.banana.name} to {self.breakfast.name}")

        response = self.client.get('/api/v1/meals/1')
        result = response.json()
        self.assertEqual(result["foods"][0]["name"], self.banana.name)

    def test_associates_food_with_a_meal(self):
        response = self.client.get('/api/v1/meals/1')
        result = response.json()
        self.assertEqual(result["name"], self.breakfast.name)
        self.assertEqual(result["foods"], [])

        response = self.client.post('/api/v1/meals/1/foods/1')
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result["message"], f"Successfully added {self.banana.name} to {self.breakfast.name}")

        response = self.client.get('/api/v1/meals/1')
        result = response.json()
        self.assertEqual(result["foods"][0]["name"], self.banana.name)

        response = self.client.delete('/api/v1/meals/1/foods/1')
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result["message"], f"Successfully removed {self.banana.name} from {self.breakfast.name}")

        response = self.client.get('/api/v1/meals/1')
        result = response.json()
        self.assertEqual(result["foods"], [])
