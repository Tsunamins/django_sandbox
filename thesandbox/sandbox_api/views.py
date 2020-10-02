# original/usual
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

# from custom user tutorial:
from rest_framework import generics, status
from .serializers import RegisterSerializer, EmailVerificationSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings

# from custom user
class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse('verify-email')
        
        absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
        email_body = 'Welcome ' + user.email + '\n Use the link below to verify your email. \n' + absurl
        data = {'email_body':email_body, 'to_email': user.email, 'email_subject':'Verify your email'}
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    serializer_class = EmailVerificationSerializer
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()

            return Response({'email': 'Sucessfully Activated'}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Link Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)




# from docs intro using standard models
# Users/Groups based on standard model
# from django.contrib.auth.models import User, Group
# from sandbox_api.serializers import UserSerializer, GroupSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]


# puppies tutorial
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

class PuppyListView(ListAPIView):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer
    permission_classes = (permissions.AllowAny, )


class PuppyDetailView(RetrieveAPIView):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer
    permission_classes = (permissions.AllowAny, )

# for mail
from django.core.mail import send_mail
class PuppyCreateView(CreateAPIView):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerializer
    # permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )
    # does send an email had to go to: http://127.0.0.1:8000/create/ to add the puppy based on my poor urls
    # send_mail('Welcoming your new pet', 'Thank you for choosing Pet Care Sobe today!', 'reillyamr@gmail.com', ['reillyamr@gmail.com'], fail_silently=False)


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


# from tests tutorial for ingredients example
# from rest_framework import viewsets, mixins, status
# from rest_framework import viewsets, mixins
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from . models import Ingredient
# from . import serializers

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


# bucket list imports and example
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

class BucketlistListView(ListAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.AllowAny, )


class BucketlistDetailView(RetrieveAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.AllowAny, )


class BucketlistCreateView(CreateAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    # permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )


class BucketlistUpdateView(UpdateAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    # permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )


class BucketlistDeleteView(DestroyAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    # permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (permissions.AllowAny, )
