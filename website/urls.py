from django.urls import path, include
from . import views
from rest_framework import routers
from website import views

app_name = 'website'

router = routers.DefaultRouter()
router.register("car-list", views.CarListViewSet)
# router.register("cars/details", views.DetailViewSet)
routerid = routers.DefaultRouter()
routerid.register("cars/variants", views.CarVariationViewset)
routerid.register("cars/place-order", views.PlaceOrderViewset)
routerid.register("cars/order", views.OrderViewset)

# urlpatterns = router.urls
urlpatterns = [
    # /website/
    # path('', views.IndexView.as_view(), name='index'),
    path('', include(router.urls)),
    path('', include(routerid.urls)),
    # /website/car-list
    # path('car-list/',views.CarListViewSet.as_view({'get': 'list'}), name='car-list'),
    # /website/car-list/3
    # path('car-list/details/<int:pk>/', views.specs, name='specs'),
]
