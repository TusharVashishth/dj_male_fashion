from django.urls import path
from .views import *

urlpatterns = [
    path('', cart, name="cart"),
    path('<str:product_id>/', addToCart, name="addToCart"),
    path('remove/<str:pk>/', removeToCart, name="removeToCart"),
    path('update/quantity/', changeQuantity, name="updateCartQuantity"),
    path('user/checkout/', checkout, name="checkout"),
    path('user/checkout/complete', checkoutComplete, name="checkoutComplete"),
]
