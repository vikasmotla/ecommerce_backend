from django.conf.urls import include, url
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'user', UserViewSet, base_name = 'user')
router.register(r'profile', ProfileViewSet, base_name = 'profile')
router.register(r'address', AddressViewSet, base_name = 'address')


urlpatterns = [
    url(r'^', include(router.urls)),
]
