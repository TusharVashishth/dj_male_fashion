from django.urls import path
from .views import *

urlpatterns = [
    path('my-orders/', userOrders, name="user_orders")
]
