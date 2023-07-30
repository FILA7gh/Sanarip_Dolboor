from rest_framework import generics

from . import models, serializers, utils


class ProductAPIView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = utils.ProductPagination


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer
