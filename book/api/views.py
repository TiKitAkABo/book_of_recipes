from rest_framework import viewsets

from .serializers import RecipesSerializer
from .serializers import IngredientsSerializer
from .models import Recipes
from .models import Ingredients


class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer


class IngredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer