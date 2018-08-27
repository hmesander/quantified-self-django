from django.urls import include, path
from .views import FoodViews


urlpatterns = [
    path('foods/', FoodViews.as_view({'get': 'list', 'post': 'create'})),
    path('foods/<food_id>', FoodViews.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'}))
]
