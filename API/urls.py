from django.conf.urls import include, url

urlpatterns = [
    url(r'^ecommerce/', include('ecommerce.urls')),
    url(r'^order_management/', include('order_management.urls')),
    url(r'^payment/', include('payment.urls')),
    url(r'^PIM/', include('PIM.urls')),
    url(r'^UMS/', include('UMS.urls')),

]
