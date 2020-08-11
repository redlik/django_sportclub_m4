from django.shortcuts import render
from blog.models import Post

def index(request):
    """ View to display homepage """
    headings = Post.published.all()[:3]
    posts = Post.published.all()[3:99]
    return render(request, 'homepage/index.html', {'headings':headings, 'posts': posts})
