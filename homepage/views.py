from django.shortcuts import render
from blog.models import Post
from products.models import Product

def index(request):
    """ View to display homepage """
    headings = Post.published.all()[:3]
    posts = Post.published.all()[3:99]
    featured_products = Product.objects.order_by('?')[:3]
    context = {
        'headings': headings,
        'posts': posts,
        'featured_products': featured_products,
    }

    return render(request, 'homepage/index.html', context)
