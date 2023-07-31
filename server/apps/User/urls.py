from django.urls import path
from . import views

urlpatterns = [

    # registration and authorization
    path('register/', views.UserRegisterAPIView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),

    # FavoriteProduct
    path('favorite-products/', views.FavoriteProductAPIView.as_view()),

]
