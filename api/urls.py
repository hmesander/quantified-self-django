from django.urls import include, path
from .views import FoodViews, MealViews, MealFoodViews


urlpatterns = [
    path('foods/', FoodViews.as_view({'get': 'list', 'post': 'create'})),
    path('foods/<food_id>', FoodViews.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
    path('meals/', MealViews.as_view({'get': 'list'})),
    path('meals/<meal_id>', MealViews.as_view({'get': 'retrieve'})),
    path('meals/<meal_id>/foods/<id>', MealFoodViews.as_view({'post': 'create', 'delete': 'destroy'}))
]
