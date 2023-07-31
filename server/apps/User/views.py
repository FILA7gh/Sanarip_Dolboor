from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth import authenticate, logout
from rest_framework_simplejwt.tokens import RefreshToken

from . import serializers, models, utils, permissions
from server.core import paginations


'''Registration and authorization'''


class UserRegisterAPIView(generics.GenericAPIView):
    serializer_class = serializers.RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        utils.send_email(subject=f'Параметры учётной записи для {user.username} ',
                         body=f'Здравствуйте {user.first_name} {user.last_name}\n'
                         f'Спасибо за регистрацию на Наш интернет магазин!.\n',
                         to_email=[user.email])

        if utils.send_email:

            # Создаем токен для пользователя
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            user.save()

            return Response(data={'message': 'Сообщение\n'
                                  'Спасибо за регистрацию. Теперь вы можете войти на сайт, '
                                  'используя логин и пароль, указанные при регистрации.\n',
                                  'access_token': access_token,
                                  'refresh_token': str(refresh)},
                            status=status.HTTP_201_CREATED)
        user.delete()

        return Response(data=f'Problem sending email to {user.email}, check if you typed it correctly',
                        status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            return Response(data={'detail': 'succsess'}, status=status.HTTP_201_CREATED)

        return Response(data={'detail': 'Неправильный логин или пароль!'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    @staticmethod
    def post(request, *args, **kwargs):
        logout(request)
        return Response(data={'detail': 'Вы успешно вышли'})


'''Favorite product'''


class FavoriteProductAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedAndFavoriteProductOwner]
    pagination_class = paginations.PaginationForTen

    # условие для методов какой сериалайзер класс использовать
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.FavoriteProductListSerializer
        elif self.request.method == 'POST':
            return serializers.FavoriteProductAddSerializer

    def get_queryset(self):
        user = self.request.user
        return models.FavoriteProduct.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        user = request.user

        try:
            favorite_product = models.FavoriteProduct.objects.get(product=product_id, user=user)
            favorite_product.delete()
            return Response(data={'detail': 'Товар удален из избранных. '}, status=status.HTTP_204_NO_CONTENT)
        except models.FavoriteProduct.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)

            return Response(data={'detail': 'Товар успешно добавлен в избранные. '}, status=status.HTTP_201_CREATED)
