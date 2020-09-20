from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from . models import Ingredient, Recipe
from . serializers import IngredientSerializer
INGREDIENTS_URL = reverse('recipe:ingredient-list')


class PrivateIngredientsApiTest(TestCase):  # Test the private ingredients api
 
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'ksarthak4ever@gmail',
            'hakunamatata'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_ingredients_list(self):  # Test retrieving a list of ingredients
        Ingredient.objects.create(user=self.user, name='Potato')
        Ingredient.objects.create(user=self.user, name='Peas')
        res = self.client.get(INGREDIENTS_URL)
        ingredients = Ingredient.objects.all().order_by('-name')
        serializer = IngredientSerializer(ingredients, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_ingredient_successful(self):  # Testing create a new ingredient
        payload = { 'name': 'Cabbage' }
        self.client.post(INGREDIENTS_URL, payload)
        exists = Ingredient.objects.filter(
            user = self.user,
            name = payload['name'],
            ).exists()  # chechking if ingredient exists. exists() function will return boolean true or false value
        self.assertTrue(exists)
