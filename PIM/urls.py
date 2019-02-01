from django.conf.urls import include, url
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'inventory', InventoryViewSet, base_name = 'inventory')
router.register(r'reviews', ReviewsViewSet, base_name = 'reviews')

urlpatterns = [
    url(r'^', include(router.urls)),
]
