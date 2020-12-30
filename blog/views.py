from django.shortcuts import render, get_object_or_404
from .models import Post

def posts_list(request):
    """ View to show all posts in timeline layout """
    posts = Post.published.all()

    return render(request, 'news/list_of_posts.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    """ View to show individual post """
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)

    return render(request, 'news/detail_view.html', {'post': post})

