from rest_framework import generics

from . import models, serializers
from server.core import paginations


class ProductAPIView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = paginations.PaginationForTen  # кастомная пагинация


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer
