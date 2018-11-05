from django.db import models

# Create your models here.
from django.db import models


class Client(models.Model):
    dealership_name = models.CharField(max_length=50)
    domain_assoc = models.CharField(max_length=50)
    new_inventory_url = models.CharField(max_length=100)
    used_inventory_url = models.CharField(max_length=100)


class Inventories(models.Model):
    full_name = models.CharField(max_length=50)
    year = models.IntegerField(4)
    make = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=20)
    trim = models.CharField(max_length=30)
    price = models.FloatField(max_length=15)
    vin = models.CharField(max_length=50)
    color = models.CharField(max_length=40)
    new_old = models.CharField(max_length=10)


class VehicleMsrpModel(models.Model):
    full_name = models.ForeignKey(Inventories, on_delete=models.CASCADE)
    year = models.IntegerField(4)
    make = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=20)
    msrp_high = models.FloatField(max_length=15)
    msrp_low = models.FloatField(max_length=15)
