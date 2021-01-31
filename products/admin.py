from django.contrib import admin
from .models import Product, Category, Device, Reviews, Upgrade



class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'model_name',
        'sku',
        'category',
        'device',
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


class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Reviews)
admin.site.register(Upgrade)
