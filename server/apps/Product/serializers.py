from rest_framework import serializers

from . import models


class CountryOfOriginSerializer(serializers.ModelSerializer):
    country = serializers.CharField(max_length=100)

    class Meta:
        model = models.CountryOfOrigin
        fields = '__all__'


class SizeSerilizer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=50)

    class Meta:
        model = models.Size
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    season = serializers.CharField(max_length=50)

    class Meta:
        model = models.Season
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    color = serializers.CharField(max_length=50)

    class Meta:
        model = models.Color
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    size = SizeSerilizer(many=True)

    class Meta:
        model = models.Product
        fields = ['id', 'image', 'title', 'size', 'gender', 'category']


class ProductDetailSerializer(serializers.ModelSerializer):
    country_of_origin = CountryOfOriginSerializer()
    size = SizeSerilizer(many=True)
    color = ColorSerializer(many=True)
    season = SeasonSerializer(many=True)

    image = serializers.ImageField(required=True)
    title = serializers.CharField(max_length=100, required=True)
    gender = serializers.CharField(max_length=50, required=True)
    category = serializers.CharField(max_length=50, required=True)
    compound = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = models.Product
        fields = ['image', 'title', 'description', 'compound',
                  'gender', 'category', 'size', 'color', 'season', 'country_of_origin']
