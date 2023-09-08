from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Car, CarVariation, PlaceOrder
from .serializers import CarListSerializer, CarVariationSerializer, OrderSerializer, PlaceOrderSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.


class CarListViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer


class CarVariationViewset(viewsets.ModelViewSet):
    queryset = CarVariation.objects.all()
    serializer_class = CarVariationSerializer


class PlaceOrderViewset(viewsets.ModelViewSet):
    queryset = PlaceOrder.objects.all()
    serializer_class = PlaceOrderSerializer


class OrderViewset(viewsets.ModelViewSet):
    queryset = PlaceOrder.objects.all()
    serializer_class = OrderSerializer

# ViewSets
# class IndexView(generic.ListView):
#     template_name = 'website/index.html'

#     def get_queryset(self):
#         pass


# class CarListViewSet(viewsets.ModelViewSet):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer


# class DetailViewSet(viewsets.ModelViewSet):
#     queryset = Details.objects.all()
#     serializer_class = SpecsSerializer


# class CustomizationViewSet(viewsets.ModelViewSet):
#     queryset = Customization.objects.all()
#     serializer_class = CustomizationSerializer


# Functional APIs
# @api_view(['GET'])
# def carList(request):
#     cars = Car.objects.all()
#     serializer = CarSerializer(cars, many='true')
#     return Response(serializer.data)

# @api_view(['GET'])
# def specs(request, pk):
#     specs = Details.objects.filter(id=pk)
#     serializer = SpecsSerializer(specs, many='true')
#     return Response(serializer.data)


# class CarListView(generic.ListView):
#     model = Car
#     template_name = 'website/car_list.html'
#     context_object_name = 'list_cars'
