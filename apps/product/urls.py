from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('shop/', shop, name="shop"),
    path('category/<str:category>/', categoryFilter, name="category"),
    path('brand/<str:brand>/', brandFilter, name="brand"),
    path('product/<str:pk>/', singleProduct, name="single_product"),
]
