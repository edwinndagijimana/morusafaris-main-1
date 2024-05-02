from django.db import models
from django.db.models import CharField
from django.utils.html import mark_safe


# Create your models here.

class service(models.Model):
    heading = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)
    content = models.CharField(max_length=10000)


class tour(models.Model):
    heading = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    price = models.IntegerField(default=100)
    image = models.ImageField(upload_to='media/', default="product.jpg")

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50">' % self.image.url)


class team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=100)


class footer(models.Model):
    phone = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)


class htels(models.Model):
    heading = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    price = models.IntegerField(default=100)
    image_url = models.CharField(max_length=100)
