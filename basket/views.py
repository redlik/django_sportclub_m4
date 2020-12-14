from django.shortcuts import render, redirect


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

    print(basket)

    return redirect(redirect_url)
