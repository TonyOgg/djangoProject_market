from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=20)

class Car(models.Model):
    name = models.ForeignKey(Cars, on_delete=models.CASCADE)
    base = models.CharField(max_length=40)
    car_body = models.CharField(max_length=40)
    year = models.IntegerField(default=0)
