from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('title', 'description', 'image', 'price', 'quantity_in_stock', 'quantity_sold')