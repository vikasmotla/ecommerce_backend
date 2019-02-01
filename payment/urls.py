from django.conf.urls import include, url
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'payment', PaymentViewSet, base_name = 'payment')
router.register(r'wallet', WalletViewSet, base_name = 'wallet')

urlpatterns = [
    url(r'^', include(router.urls)),
]
