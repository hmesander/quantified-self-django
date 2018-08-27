from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from api.models import Food
from api.serializers import FoodSerializer
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
