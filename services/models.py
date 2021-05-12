from django.db import models


# Create your models here.
class Service(models.Model):

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='services')
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

        def __str__(self):
            return self.title

