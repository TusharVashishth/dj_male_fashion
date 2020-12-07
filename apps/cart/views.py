from django.shortcuts import redirect, render
from .models import Cart
from django.contrib import messages
from utils.helper_methods import cart_total, cart_items
import json
from apps.user_address.models import UserAddress
from django.http import JsonResponse
from apps.orders.models import Order


def cart(request):
    carts = cart_items(request)
    context = {'carts': carts, 'cartTotal': cart_total(request)}
    return render(request, 'cart.html', context)


def addToCart(request, product_id):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(product_id=product_id).first()

        if cart:
            updateCart = Cart(cart.id, user_id=request.user.id, product_id=product_id, quantity=cart.quantity + 1)
            updateCart.save()
        else:
            Cart.objects.create(user_id=request.user.id, product_id=product_id, quantity=1)

        messages.success(request, 'Product added successfully.')
        return redirect('cart')
    else:
        messages.error(request , 'Please login first.')
        return redirect('account_login')


def removeToCart(request, pk):
    if request.user.is_authenticated:
        Cart.objects.get(pk=pk).delete()
        messages.success(request, 'Product remove from cart')
        return redirect('cart')
    else:
        messages.error(request, 'Please login first.')
        return redirect('account_login')


def changeQuantity(request):
    data = json.loads(request.body)
    quantity = data['quantity']
    id = data['id']
    if int(quantity) > 0:
        Cart.objects.update_or_create(id=id, defaults={'quantity': quantity})
    else:
        Cart.objects.get(pk=id).delete()
    messages.success(request, 'Cart updated successfully.')

    # data = json.load(request.body)
    # print(data)


def checkout(request):
    if request.user.is_authenticated:
        address = UserAddress.objects.filter(user_id=request.user.id).first()
        carts = Cart.objects.filter(user_id=request.user.id, status='0')

        if address:
            context = {'address': address, 'cartTotal': cart_total(request), 'carts': carts}
            return render(request, 'checkout.html', context)
        else:
            messages.error(request, 'Please fill your address first')
            return redirect('user_address')
    else:
        messages.error(request, 'Please login first.')
        return redirect('account_login')


def checkoutComplete(request):
    carts = cart_items(request)
    for cart in carts:
        Order.objects.create(user_id=request.user.id, product=cart.product_id, quantity=cart.quantity,
                             amount=cart.product.price, total_amount=cart.product.price * cart.quantity)
    carts.update(status=1)
    messages.success(request ,'Order Placed successfully.')
    return JsonResponse('hii', safe=False)
