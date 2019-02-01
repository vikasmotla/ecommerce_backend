from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ecommerce.views import *

urlpatterns = [
    url(r'^$', index , name ='root'),
    url(r'^api/', include('API.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
