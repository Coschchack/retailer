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


class Order(models.Model):
    products = models.ManyToManyField('Product', related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
