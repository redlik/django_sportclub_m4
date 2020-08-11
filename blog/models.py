from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedPosts(models.Manager):
    '''Custom query manager to pull only publishded posts.'''

    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):
    PUBLISH_STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_post')
    body = models.TextField()
    image = models.ImageField(upload_to='images/posts/', blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=PUBLISH_STATUS, default='draft')

    objects = models.Manager() # The default manager for all posts.
    published = PublishedPosts() # Custom manager for only published posts.

    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title

    # using reverse function to get the canonical url for each post item - year/month/day/slug
    def get_post_url(self):
            return reverse('news:post_detail_view',
                        args=[self.publish.year,
                                self.publish.month,
                                self.publish.day, self.slug])
