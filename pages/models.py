from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=300)
    source = models.URLField(default="alibaba.com")
