from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from api.models import Food
from api.serializers import FoodSerializer
from rest_framework.response import Response

def index(request):
    return HttpResponse("Welcome to Quantified Self - Django!")

class FoodViews(viewsets.ViewSet):
    def list(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)
