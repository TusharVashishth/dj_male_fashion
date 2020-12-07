from django.urls import path, include

urlpatterns = [
    path('', include('apps.product.urls')),
    path('cart/', include('apps.cart.urls')),
    path('user_address/', include('apps.user_address.urls')),
    path('orders/', include('apps.orders.urls'))
]
