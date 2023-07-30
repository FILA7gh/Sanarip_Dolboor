from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', views.LogoutAPIView.as_view())
]
