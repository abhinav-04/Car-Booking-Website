from django.contrib import admin
from .models import Car, Paint, Interior, PlaceOrder, Wheel, AddOn, CarVariation

admin.site.register(Car)
admin.site.register(Paint)
admin.site.register(Interior)
admin.site.register(Wheel)
admin.site.register(AddOn)
admin.site.register(CarVariation)
admin.site.register(PlaceOrder)


# admin.site.register(Car)
# admin.site.register(PlaidSpec)
# admin.site.register(LongRangeSpec)
# admin.site.register(Details)
