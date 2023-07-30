from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, logout

from .serializers import RegisterSerializer, LoginSerializer
from .utils import send_email


class UserRegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.save()

        send_email(subject=f'Параметры учётной записи для {user.username} ',
                   body=f'Здравствуйте {user.first_name} {user.last_name}\n'
                        f'Спасибо за регистрацию на Наш интернет магазин!.\n',
                   to_email=[user.email])

        if send_email:
            return Response(data='Сообщение\n'
                                 'Спасибо за регистрацию. Теперь вы можете войти на сайт, '
                                 'используя логин и пароль, указанные при регистрации.',
                            status=status.HTTP_201_CREATED)
        user.delete()
        return Response(data=f'Problem sending email to {user.email}, check if you typed it correctly',
                        status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

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
