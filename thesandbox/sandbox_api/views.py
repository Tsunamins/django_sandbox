# original
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

# Users/Groups
from sandbox_api.serializers import UserSerializer, GroupSerializer


# puppies tests tutorial
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# using these viewsets instead for puppy to be consistent:
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from .models import Puppy
from .serializers import PuppySerializer

# from tests tutorial
# from rest_framework import viewsets, mixins, status
# from rest_framework import viewsets, mixins
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from . models import Ingredient
# from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# puppies tutorial
class PuppyListView(ListAPIView):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer
    permission_classes = (permissions.AllowAny, )


class PuppyDetailView(RetrieveAPIView):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer
    permission_classes = (permissions.AllowAny, )


class PuppyCreateView(CreateAPIView):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer
    # permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )


class PuppyUpdateView(UpdateAPIView):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer
    # permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )


class PuppyDeleteView(DestroyAPIView):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer
    # permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )


# class IngredientViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Ingredient.objects.all()
#     serializer_class = serializers.IngredientSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     def get_queryset(self):
#         assigned_only = bool(self.request.query_params.get('assigned_only'))
#         queryset = self.queryset
#         if assigned_only:
#             queryset = queryset.filter(recipe__isnull=False)
#             return queryset.filter(user=self.request.user).order_by('-name')

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
