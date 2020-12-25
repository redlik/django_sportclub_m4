from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "The basket is empty at the moment")
        return redirect(reverse('shop:all_products'))

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_4DsMDDIsp4VTuDwC1AfU1mmo',
        'client_secret': 'client secret',
    }

    return render(request, 'checkout/checkout.html', context)
