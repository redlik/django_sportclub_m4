from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    PUBLISH_STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_post')
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=PUBLISH_STATUS, default='draft')

    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title

