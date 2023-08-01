from django.db import models
from django.contrib.auth.models import User

from server.apps.Product.models import Product


# моделька избранных товаров
class FavoriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorite_product')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return f'{self.user} {self.product}'
