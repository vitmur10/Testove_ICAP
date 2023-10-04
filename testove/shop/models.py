from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    photo_url = models.URLField()
    category = models.CharField(max_length=255)
    is_offer_of_the_month = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)
    is_pickup_available = models.BooleanField(default=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
