from rest_framework import serializers

# from custom User model
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password']

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    # username = serializers.CharField(max_length=255, min_length=3, read_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }
    
    class Meta:
        model = User
        fields = ['email', 'password', 'tokens'] # tutorial has username also, but currently no username in this example

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        if filtered_user_by_email.exists():
            raise AuthenticationFailed(
                detail='Please continue your login using ')

        if not user:
            raise AuthenticationFailed('Invalid Credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')
     
        return {
            'email': user.email,
            # 'username': user.username,
            #tutorial says should call tokens() method
            'tokens': user.tokens
        }

        return super().validate(attrs)




        


from .models import Puppy
class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields = ('name', 'age', 'breed', 'color', 'created_at', 'updated_at')


# from sandbox_api.models import Ingredient
# class IngredientSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Ingredient
#         fields = ('id', 'name')
#         read_only_fields = ('id',)

from .models import Bucketlist
class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


# from django.contrib.auth.models import User, Group
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']
