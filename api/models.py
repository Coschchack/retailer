from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[
            MinValueValidator(0.01),
            MaxValueValidator(100000.00),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)


class DetailedProduct(models.Model):
    order = models.ForeignKey('Order', related_name="detailed_products", on_delete=models.CASCADE)
    product = models.ForeignKey('Product', related_name="detailed_products", on_delete=models.CASCADE)
    size = models.CharField(max_length=1, default='M')


class Order(models.Model):
    products = models.ManyToManyField('Product', related_name='orders', through='DetailedProduct')
    created_at = models.DateTimeField(auto_now_add=True)
