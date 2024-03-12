from django.db import models
from django.contrib.auth.models import User,AbstractUser
import os


def user_directory_path(instance, filename):
    author_name = instance.author.username
    return os.path.join('blog_previews', author_name, filename)

class Profil(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    ip_username = models.GenericIPAddressField(null=True, blank=True)
    user_photo = models.ImageField(upload_to=user_directory_path, blank=True)
    user_fon = models.ImageField(upload_to=user_directory_path, blank=True)
    user_about = models.TextField(null=True, blank=True)