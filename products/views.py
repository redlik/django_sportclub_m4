from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category


def all_products(request):
    """ View to show main Shop page """

    products = Product.objects.all()
    categories = Category.objects.all()
    current_category = None

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)
            current_category = categories.filter(name__icontains=category).first()

    return render(request, 'products/all_products.html',
                  {'products': products, 'categories': categories, 'current_category': current_category, })


def product_detail(request, product_id):
    """ View to show individual products """
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/product_detail.html', {'product': product})
