from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "The basket is empty at the moment")
        return redirect(reverse('shop:all_products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form
    }

    return render(request, 'checkout/checkout.html', context)
