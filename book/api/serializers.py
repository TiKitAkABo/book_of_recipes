from rest_framework import serializers
from .models import Recipes
from .models import Ingredients


class RecipesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipes
        fields = ('name', 'ingredients', 'steps', 'img')


class IngredientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('named', 'quantity')