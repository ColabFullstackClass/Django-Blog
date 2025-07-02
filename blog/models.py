from django.db import models
from django.utils import timezone
from django.conf import settings

status_choices = [('DF', 'Draft'), ('PB', 'Published')]

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    # image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    publish =  models.DateTimeField(default=timezone.now())
    updated =  models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=status_choices, default="Draft")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')

    def __str__(self):
        return self.title    