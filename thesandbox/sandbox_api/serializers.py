from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from sandbox_api.models import Ingredient


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# class IngredientSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Ingredient
#         fields = ('id', 'name')
#         read_only_fields = ('id',)
