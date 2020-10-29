from django.contrib import admin
from .models import Product, Category, Ratings


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class RatingsAdmin(admin.ModelAdmin):
    readonly_fields = (
        'product',
        'user_profile',
        'stars',
        )

    list_display = (
        'product',
        'user_profile',
        'stars',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ratings, RatingsAdmin)
