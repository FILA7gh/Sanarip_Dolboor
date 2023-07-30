from django.db import models


class Size(models.Model):
    CHOICE_SIZE = [
        ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'),
        ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')
    ]

    size = models.CharField(choices=CHOICE_SIZE, max_length=50)

    def __str__(self):
        return self.size


class Color(models.Model):
    CHOICE_COLOR = [
        ('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'),
        ('yellow', 'Yellow'), ('orange', 'Orange'), ('purple', 'Purple'),
        ('pink', 'Pink'), ('brown', 'Brown'), ('white', 'White'),
        ('black', 'Black'), ('gray', 'Gray')
    ]

    color = models.CharField(choices=CHOICE_COLOR, max_length=50)

    def __str__(self):
        return self.color


class Season(models.Model):
    CHOICE_SEASON = [
        ('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn'),
        ('winter', 'Winter'), ('pre-fall', 'Pre-Fall'), ('demi-season', 'Demi-Season'),
        ('resort', 'Resort'), ('holiday', 'Holiday'), ('back-to-school', 'Back-to-School'),
    ]

    season = models.CharField(choices=CHOICE_SEASON, max_length=50)

    def __str__(self):
        return self.season


class Product(models.Model):
    CHOICE_GENDER = (
                     ('Men', 'Men'), ('Women', 'Women'), ('Unisex', 'Unisex')
    )
    CHOICE_CATEGORY = (
                        ('Children', 'Children'), ('Teenage', 'Teenage'),
                        ('Adult', 'Adult'), ('Elderwear', 'Elderwear')
    )

    image = models.ImageField()
    title = models.CharField(max_length=100)
    gender = models.CharField(choices=CHOICE_GENDER, max_length=50)
    category = models.CharField(choices=CHOICE_CATEGORY, max_length=50)
    compound = models.TextField()
    description = models.TextField()

    size = models.ManyToManyField(Size, related_name='Product')
    color = models.ManyToManyField(Color, related_name='Product')
    season = models.ManyToManyField(Season, related_name='Product')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class CountryOfOrigin(models.Model):
    country = models.CharField(max_length=100)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='country_of_origin')

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'

    def __str__(self):
        return f'{self.product.title}'
