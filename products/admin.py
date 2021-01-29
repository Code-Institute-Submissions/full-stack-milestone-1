from django.contrib import admin
from .models import Product, Category



class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'model_name',
        'sku',
        'category',
        'price',
        'brand',
        'image',
    )

    ordering = ('model_name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)