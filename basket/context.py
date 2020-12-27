from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    basket_items = []
    total = 0
    delivery = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for product_id, product_data in basket.items():
        if isinstance(product_data, int):
            product = get_object_or_404(Product, pk=product_id)
            total += product_data * product.price
            product_count += product_data
            basket_items.append({
                'product_id': product_id,
                'quantity': product_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=product_id)
            for size, quantity in product_data['products_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'product_id': product_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })
    if total < 100 and total != 0:
        delivery = 5
    else:
        delivery = 0
    grand_total = total + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'delivery': delivery,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
