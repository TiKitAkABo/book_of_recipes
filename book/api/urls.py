from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'ingredients', views.IngredientsViewSet)
router.register(r'recipes', views.RecipesViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'api-auth', include('rest_framework.urls', namespace='rest_framework'))
]