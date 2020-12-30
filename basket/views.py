from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_basket(request):
    return render(request, 'basket/basket.html')


def add_to_basket(request, product_id):
    """ Function to add product,size and quantity to the basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if product_id in list(basket.keys()):
            if size in basket[product_id]['products_by_size'].keys():
                basket[product_id]['products_by_size'][size] += quantity
            else:
                basket[product_id]['products_by_size'][size] = quantity
        else:
            basket[product_id] = {'products_by_size': {size: quantity}}
    else:
        if product_id in list(basket.keys()):
            basket[product_id] += quantity
        else:
            basket[product_id] = quantity

    request.session['basket'] = basket

    return redirect(redirect_url)


def adjust_basket(request, product_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[product_id]['products_by_size'][size] = quantity
            messages.success(request,
                             f'Updated size {size.upper()} {product.name} quantity to {basket[product_id]["products_by_size"][size]}')
        else:
            del basket[product_id]['products_by_size'][size]
            if not basket[product_id]['products_by_size']:
                basket.pop(product_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your basket')
    else:
        if quantity > 0:
            basket[product_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {basket[product_id]}')
        else:
            basket.pop(product_id)
            messages.success(request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('basket:view_basket'))


def remove_from_basket(request, product_id):
    """Remove the item from the shopping basket"""

    try:
        product = get_object_or_404(Product, pk=product_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        if size:
            del basket[product_id]['products_by_size'][size]
            if not basket[product_id]['products_by_size']:
                basket.pop(product_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your basket')
        else:
            basket.pop(product_id)
            messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
