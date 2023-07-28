from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # for products urls
    path('products/', include('server.apps.Product.urls')),

    # for users
    path('user/', include('server.apps.User.urls')),

]
