from django.db import models
# Create your models here.


class Question(models.Model):
    text = models.CharField(max_length=200)


class Product(models.Model):
    image_url = models.CharField(max_length=255)
    name = models.CharField(max_length=200)
    stock = models.IntegerField()
    price = models.FloatField()
