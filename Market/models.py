from django.db import models
from django.contrib.auth.models import User

class Cars(models.Model):
    name = models.CharField(max_length=20)

class Car(models.Model):
    name = models.ForeignKey(Cars, on_delete=models.CASCADE)
    base = models.CharField(max_length=40)
    car_body = models.CharField(max_length=40)
    year = models.IntegerField(default=0)

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField('Address', max_length=100)
