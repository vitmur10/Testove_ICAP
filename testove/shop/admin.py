from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_offer_of_the_month', 'is_available', 'is_pickup_available', 'price')
    list_filter = ('category', 'is_offer_of_the_month', 'is_available', 'is_pickup_available')


admin.site.register(Product, ProductAdmin)
