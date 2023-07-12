from django.contrib import admin
from ecomapp.models import *

# Register your models here.
admin.site.register([Admin, Customer, ProductImage, Product, Cart, CartProduct, Order, Category ])