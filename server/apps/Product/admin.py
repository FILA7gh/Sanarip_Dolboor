from django.contrib import admin
from . import models

admin.site.register(models.Product)
admin.site.register(models.Size)
admin.site.register(models.Season)
admin.site.register(models.Color)
admin.site.register(models.CountryOfOrigin)
