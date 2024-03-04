from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone




class Blog_News(models.Model):
    title = models.CharField(max_length=100)
    tags = TaggableManager()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    blog = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    preview = models.ImageField(upload_to='blog_previews/')
    
    class Meta:
        ordering = ['-publish']



class Subsection(models.Model):
    blog_news = models.ForeignKey(Blog_News, on_delete=models.CASCADE, related_name='subsections')
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='subsection_images/', null=True, blank=True)