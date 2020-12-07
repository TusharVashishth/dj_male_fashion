from django.contrib import admin
from .models import UserAddress


class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street_address', 'apartment', 'city', 'state', 'pincode' ,'status')
    search_fields = ('user', 'city', 'state')
    list_per_page = 20


admin.site.register(UserAddress, UserAddressAdmin)
