from django.contrib import admin
from django.contrib.auth.models import User


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active' ,'date_joined']
    list_display_links = ('username', 'email')
    search_fields = ('username', 'email', 'is_active', 'first_name')


admin.site.unregister(User)
# admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)
