from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'quantity', 'amount', 'created_at')
    search_fields = ('user', 'amount', 'quantity')
    list_per_page = 20
    list_filter = ('amount', 'quantity')


admin.site.register(Order, OrderAdmin)
