from django.conf.urls import include, url
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'couponCode', CouponCodeViewSet, base_name = 'couponCode')
router.register(r'trackingLog', TrackingLogViewSet, base_name = 'trackingLog')
router.register(r'orderedProduct', OrderedProductViewSet, base_name = 'orderedProduct')
router.register(r'order', OrderViewSet, base_name = 'order')
router.register(r'cart', CartViewSet, base_name = 'cart')
router.register(r'savedProduct', SavedProductViewSet, base_name = 'savedProduct')

urlpatterns = [
    url(r'^', include(router.urls)),
]
