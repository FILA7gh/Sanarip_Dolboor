from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

import server.settings.base
from server.settings.swagger import urlpatterns as swagger


urlpatterns = [
    path('admin/', admin.site.urls),

    # for products urls
    path('api/v1/products/', include('server.apps.Product.urls')),

    # for users
    path('api/v1/users/', include('server.apps.User.urls')),

] + static(server.settings.base.MEDIA_URL, document_root=server.settings.base.MEDIA_ROOT)

urlpatterns += swagger
