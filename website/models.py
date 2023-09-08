from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, IntegerField
from django.http import request
import datetime

# Create your models here.


class Paint(models.Model):
    colour = models.CharField(max_length=20, null=True)
    price = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.colour)


class Interior(models.Model):
    interior = models.CharField(max_length=20, null=True)
    price = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.interior)


class Wheel(models.Model):
    wheel = models.CharField(max_length=20, null=True)
    price = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.wheel)


class AddOn(models.Model):
    name = models.CharField(max_length=20, null=True)
    price = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.name)


class Car(models.Model):
    name = models.CharField(max_length=20, null=True)
    Time_to_60 = models.CharField(max_length=10, null=True)
    base_price = models.IntegerField(default=0, null=True)
    start_range = models.CharField(max_length=20, null=True)
    peak_power = models.CharField(max_length=20, null=True)
    top_speed = models.CharField(max_length=20, null=True)
    weight = models.CharField(max_length=20, null=True)
    cargo_capacity = models.CharField(max_length=20, null=True)
    power_train = models.CharField(max_length=20, null=True)
    acceleration = models.CharField(max_length=20, null=True)
    drag_coefficient = models.CharField(max_length=20, null=True)
    wheels = models.CharField(max_length=20, null=True)
    charging = models.CharField(max_length=20, null=True)
    img_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)


class CarVariation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, null=True)
    add_on_price = models.IntegerField(default=0, null=True)
    range = models.CharField(max_length=20, null=True)
    peak_power = models.CharField(max_length=20, null=True)
    top_speed = models.CharField(max_length=20, null=True)
    weight = models.CharField(max_length=20, null=True)
    cargo_capacity = models.CharField(max_length=20, null=True)
    power_train = models.CharField(max_length=20, null=True)
    acceleration = models.CharField(max_length=20, null=True)
    drag_coefficient = models.CharField(max_length=20, null=True)

    charging = models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.name)


class PlaceOrder(models.Model):
    car_name = models.ForeignKey(Car, on_delete=CASCADE, null=True)
    car_variant = models.ForeignKey(CarVariation, on_delete=CASCADE, null=True)
    paint = models.ManyToManyField(Paint)
    interior = models.ManyToManyField(Interior)
    wheel = models.ManyToManyField(Wheel)
    add_on = models.ManyToManyField(AddOn)
    price = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.car_name)


# class Order(models.Model):
#     # car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     orders = models.ForeignKey(
#         PlaceOrder, on_delete=models.CASCADE, null=True)
#     price = models.IntegerField(default=0, null=True)
#     date = models.DateTimeField(default=datetime.datetime.now)

#     def __str__(self):
#         return str(self.orders)

# class Paint(models.Model):
#     colour = models.CharField(max_length=20)
#     price = models.IntegerField(default=0)


# class Interior(models.Model):
#     colour = models.CharField(max_length=20)
#     price = models.IntegerField(default=0)


# class Wheel(models.Model):
#     colour = models.CharField(max_length=20)
#     price = models.IntegerField(default=0)


# class PlaidSpec(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     add_on_price = models.IntegerField(default=12500)
#     range = models.CharField(max_length=20)
#     peak_power = models.CharField(max_length=20)
#     top_speed = models.CharField(max_length=20)
#     weight = models.CharField(max_length=20)
#     cargo_capacity = models.CharField(max_length=20)
#     power_train = models.CharField(max_length=20)
#     acceleration = models.CharField(max_length=20)
#     drag_coefficient = models.CharField(max_length=20)
#     wheels = models.CharField(max_length=20)
#     charging = models.CharField(max_length=20)

#     def __str__(self):
#         return str(self.car)


# class LongRangeSpec(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     add_on_price = models.IntegerField(default=0)
#     range = models.CharField(max_length=20)
#     peak_power = models.CharField(max_length=20)
#     top_speed = models.CharField(max_length=20)
#     weight = models.CharField(max_length=20)
#     cargo_capacity = models.CharField(max_length=20)
#     power_train = models.CharField(max_length=20)
#     acceleration = models.CharField(max_length=20)
#     drag_coefficient = models.CharField(max_length=20)
#     wheels = models.CharField(max_length=20)
#     charging = models.CharField(max_length=20)

#     def __str__(self):
#         return str(self.car)


# class Details(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     plaid_specs = models.ForeignKey(PlaidSpec, on_delete=models.CASCADE)
#     long_range_specs = models.ForeignKey(
#         LongRangeSpec, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.car)


# class Customization(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     plaid_specs = models.ForeignKey(PlaidSpec, on_delete=models.CASCADE)
#     long_range_specs = models.ForeignKey(
#         LongRangeSpec, on_delete=models.CASCADE)
#     paint = models.CharField(max_length=20)
#     wheels = models.CharField(max_length=20)
#     interiors = models.CharField(max_length=20)

#     def __str__(self):
#         return str(self.car)
