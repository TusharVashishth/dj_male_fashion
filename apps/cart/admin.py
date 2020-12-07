from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'status')
    search_fields = ('user', 'product', 'status')
    list_per_page = 20


admin.site.register(Cart, CartAdmin)
