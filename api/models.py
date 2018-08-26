from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
