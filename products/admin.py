from django.contrib import admin
from .models import Product, Category



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name']
    list_per_page = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'stock_quantity', 'created_date']
    list_filter = ['category', 'created_date']
    search_fields = ['name', 'description', 'category__name']
    ordering = ['-created_date']
    list_per_page = 20
