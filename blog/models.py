from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

import os

def user_directory_path(instance, filename):
    author_name = instance.author.username
    return os.path.join('blog_previews', author_name, filename)

class News(models.Model):
    title = models.CharField(max_length=100)
    tags = TaggableManager()
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    blog = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    preview = models.ImageField(upload_to=user_directory_path, blank=True)
    
    class Meta:
        ordering = ['-publish']    
    
    
@receiver(pre_save, sender=News)
def generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        


     

class Subsection(models.Model):
    blog_news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='subsections')
    title = models.CharField(max_length=100,blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    
    
    
