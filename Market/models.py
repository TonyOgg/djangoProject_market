from django.db import models
from django.contrib.auth.models import User

class Cars(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='images/', default=None)

class Car(models.Model):
    name = models.OneToOneField(Cars, on_delete=models.CASCADE)
    base = models.CharField(max_length=40)
    car_body = models.CharField(max_length=40)
    year = models.DateField(default=0)
    engine_type = models.CharField(max_length=25, default=None)
    engine_size = models.FloatField(default=0)
    transmission = models.CharField(max_length=25)
    drive_unit = models.CharField(max_length=30, default='Forward')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_new = models.BooleanField(default=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='images/', default=None)


class Spares(models.Model):
    name = models.CharField(max_length=45)
    type_of_spare = models.CharField(max_length=45)
    article = models.ForeignKey(Car, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='images/', default=None)

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField('Address', max_length=100)

