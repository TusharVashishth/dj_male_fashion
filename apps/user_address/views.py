from django.shortcuts import render, redirect
from .forms import UserAddressForm
from django.contrib import messages
from .models import UserAddress


def user_form(request):
    form = UserAddressForm(request.POST or None, initial={'user': request.user.id})
    context = {'form': form}
    if request.method == 'POST':
        if request.user.is_authenticated:
            if form.is_valid():
                form.save()
                messages.success(request, 'Address Added successfully')
                return redirect('checkout')
            else:
                context = {'form': form}
                return render(request, 'user_address.html', context)

        else:
            messages.error(request, 'Please login first')

    return render(request, 'user_address.html', context)


def update_address(request):
    print('hiii')
    address = UserAddress.objects.get(user_id=request.user.id)
    print('User Addres' , address)
    form = UserAddressForm(request.POST or None, instance=address)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request , 'Address Updated successfully.')
            return redirect('checkout')
        else:
            return render(request, 'user_address.html', context)

    return render(request, 'user_address.html', context)
