from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=300)
    source = models.URLField(default='google.com')