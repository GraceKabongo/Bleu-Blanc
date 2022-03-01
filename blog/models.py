from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    
    title = models.CharField(max_length=250, unique=True)
    content = models.TextField(default=None, blank=True)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='articles', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.title

