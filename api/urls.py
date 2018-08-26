from django.urls import include, path
from .views import FoodViews


urlpatterns = [
    path('foods/', FoodViews.as_view({'get': 'list'}))
]
