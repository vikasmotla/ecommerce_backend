from django.conf.urls import include, url
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'test', TestViewSet, base_name = 'test')
router.register(r'productMedia', ProductMediaViewSet, base_name = 'productMedia')
router.register(r'categoryMedia', CategoryMediaViewSet, base_name = 'categoryMedia')
router.register(r'brandMedia', BrandMediaViewSet, base_name = 'brandMedia')
router.register(r'productMeta', ProductMetaViewSet, base_name = 'productMeta')
router.register(r'brand', BrandViewSet, base_name = 'brand')
router.register(r'category', CategoryViewSet, base_name = 'category')
router.register(r'productAtrribute', ProductAtrributeViewSet, base_name = 'productAtrribute')
router.register(r'product', ProductViewSet, base_name = 'product')

urlpatterns = [
    url(r'^', include(router.urls)),
]
