from django.db import models


class Recipes (models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    steps = models.TextField()
    img = models.ImageField(upload_to='book of recipes/article', height_field=100, width_field=100)

    def __str__(self):
        return self.name


class Ingredients (models.Model):
    named = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return self.named