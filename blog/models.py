from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name_plural = "Categories"
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(default=now)
    image = models.ImageField(upload_to="blog", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name="get_posts")  # Reverse Search
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

