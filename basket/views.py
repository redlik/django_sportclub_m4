from django.shortcuts import render


def view_basket(request):
    return render(request, 'basket/basket.html')

def add_to_basket(request, product_id):
    """ Function to add product and quantity to the basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if product_id in list(basket.keys()):
        basket[product_id] += quantity
    else:
        basket[product_id] = quantity

    request.session['basket'] = basket
