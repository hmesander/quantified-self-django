from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from api.models import Food, Meal
from api.serializers import FoodSerializer, MealSerializer
from rest_framework.response import Response
from rest_framework import status
import json

def index(request):
    return HttpResponse("Welcome to Quantified Self - Django!")

class FoodViews(viewsets.ViewSet):
    def list(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

    def retrieve(self, request, food_id=None):
        food = Food.objects.get(id=food_id)
        serializer = FoodSerializer(food)
        return Response(serializer.data)

    def create(self, request):
        food_info = json.loads(request.body)['food']
        food = Food.objects.create(name=food_info['name'], calories=food_info['calories'])
        serializer = FoodSerializer(food)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, food_id=None):
        food = Food.objects.get(id=food_id)
        food_info = json.loads(request.body)['food']
        food.name = food_info['name']
        food.calories=food_info['calories']
        food.save()
        serializer = FoodSerializer(food)
        return Response(serializer.data)

    def destroy(self, request, food_id=None):
        food = Food.objects.get(id=food_id)
        food.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

class MealViews(viewsets.ViewSet):
    def list(self, request):
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)

    def retrieve(self, request, meal_id=None):
        meal = Meal.objects.get(id=meal_id)
        serializer = MealSerializer(meal)
        return Response(serializer.data)

class MealFoodViews(viewsets.ViewSet):
    def create(self, request, meal_id=None, id=None):
        food = Food.objects.get(id=id)
        meal = Meal.objects.get(id=meal_id)
        meal.foods.add(food)
        message = { 'message': f'Successfully added {food.name} to {meal.name}' }
        return Response(message, status=status.HTTP_201_CREATED)
