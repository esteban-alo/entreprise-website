from django.db import models


# Create your models here.
class Service(models.Model):

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='services')
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Show service item title in the Service Admin list
        return self.title

    class Meta:
        ordering = ['-created_date']

