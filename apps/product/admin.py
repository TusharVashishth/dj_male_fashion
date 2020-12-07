from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'category', 'price',
                    'quantity', 'color', 'image_tag', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'brand', 'category', 'price', 'color')
    list_filter = ('id', 'name', 'price', 'created_at')
    list_per_page = 20
    # readonly_fields = ('image_tag' ,)


admin.site.register(Product, ProductAdmin)
