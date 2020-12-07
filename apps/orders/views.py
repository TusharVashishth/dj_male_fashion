from django.shortcuts import render
from .models import Order


def userOrders(request):
    orders = Order.objects.filter(user_id=request.user.id)
    context = {'orders': orders}
    return render(request, 'my_orders.html', context)
