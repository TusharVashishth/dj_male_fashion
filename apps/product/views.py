from django.shortcuts import render
from .models import Product
from apps.category.models import Category
from apps.brand.models import Brand
from apps.cart.models import Cart
from utils.helper_methods import cart_total


def index(request):
    products = Product.objects.all().order_by('-created_at')
    context = {'products': products, 'cart_total': cart_total(request)}
    return render(request, 'index.html', context)


def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    context = {'products': products,
               'categories': categories, 'brands': brands}
    return render(request, 'shop.html', context)


def categoryFilter(request, category):
    print(request.path)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    brands = Brand.objects.all()
    context = {'products': products,
               'categories': categories, 'brands': brands}
    return render(request, 'shop.html', context)


def brandFilter(request, brand):
    products = Product.objects.filter(brand=brand)
    categories = Category.objects.all()
    brands = Brand.objects.all()
    context = {'products': products,
               'categories': categories, 'brands': brands}
    return render(request, 'shop.html', context)


def singleProduct(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'shop_detail.html', context)
