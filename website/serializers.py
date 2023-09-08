from re import T
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Car, CarVariation, PlaceOrder, Paint, Wheel, Interior, AddOn


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'name', 'start_range', 'Time_to_60',
                  'top_speed', 'peak_power', 'base_price']


class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarVariation
        fields = '__all__'


class PaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paint
        fields = '__all__'


class InteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior
        fields = '__all__'


class WheelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wheel
        fields = '__all__'


class AddOnSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddOn
        fields = '__all__'


class CarVariationSerializer(serializers.ModelSerializer):
    paint = PaintSerializer(read_only=True, many=True)
    interior = InteriorSerializer(read_only=True, many=True)
    wheel = WheelSerializer(read_only=True, many=True)
    addon = AddOnSerializer(read_only=True, many=True)

    class Meta:
        model = CarVariation
        fields = '__all__'  # [paint, interior, wheel, addon]
        depth = 1


class PlaceOrderSerializer(serializers.ModelSerializer):
    car_variation = CarVariationSerializer(read_only=True, many=True)

    class Meta:
        model = PlaceOrder
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceOrder
        fields = ['id', 'car_name', 'car_variant', 'paint',
                  'interior', 'wheel', 'add_on', 'price', 'date']
        depth = 1

# Original Serializers
# class CarSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Car
#         fields = '__all__'


# class SpecsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Details
#         fields = '__all__'
#         depth = 1


# class CustomizationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Customization
#         fields = '__all__'
