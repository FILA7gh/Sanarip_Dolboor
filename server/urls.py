from django.contrib import admin
from django.urls import path, include

from server.settings.swagger import urlpatterns as urlp


urlpatterns = [
    path('admin/', admin.site.urls),

    # for products urls
    path('api/v1/products/', include('server.apps.Product.urls')),

    # for users
    path('api/v1/users/', include('server.apps.User.urls')),

]

urlpatterns += urlp
