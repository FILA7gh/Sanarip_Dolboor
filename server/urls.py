from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # for products urls
    path('api/v1/products/', include('server.apps.Product.urls')),

    # for users
    path('api/v1/users/', include('server.apps.User.urls')),

]
