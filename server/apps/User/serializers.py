from rest_framework import serializers, validators
from django.contrib.auth.models import User
import re

from . import models


'''Registration and authorization'''


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=4, required=True)
    first_name = serializers.CharField(max_length=100, required=True)
    last_name = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(min_length=8, required=True)
    password_confirm = serializers.CharField(min_length=8, required=True)
    # валидация на уникальность почты
    email = serializers.EmailField(required=True, validators=[validators.UniqueValidator(queryset=User.objects.all())])

    def validate_username(self, username):  # проверка на уникальность имени пользователя
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        return serializers.ValidationError('User already exist!')

    def validate_password_1(self, password):
        if not re.match("^(?=.*?[a-z])(?=.*?[0-9]).{8,}$", password):
            raise serializers.ValidationError(
                'Пароль должен содержать как минимум одну букву и одну цифру, и быть длиной не менее 8 символов!')

        return password

    def validate(self, attrs):
        # проверка на совпадение паролей
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError('Пароли не совпадают!')

        return attrs

    def create(self, validated_data):
        username = validated_data.get('username')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        password_1 = validated_data.get('password')
        email = validated_data.get('email')
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                        password=password_1, email=email)

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=4, required=True)
    password = serializers.CharField(min_length=8, required=True)


'''Favorite product'''


class ProductTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['title']


class FavoriteProductSerializer(serializers.ModelSerializer):
    # product = ProductTitleSerializer()

    class Meta:
        model = models.FavoriteProduct
        fields = ['id', 'user', 'product']
