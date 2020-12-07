from apps.cart.models import Cart


def cart_total(request):
    carts = cart_items(request)
    total = 0
    for cart in carts:
        total = total + cart.product.price * cart.quantity
    return total


def cart_items(request):
    carts = Cart.objects.filter(user_id=request.user.id, status='0')
    return carts
