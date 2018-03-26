from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    tag = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=64, default="Dublin")

    def __str__(self):
        return self.name
