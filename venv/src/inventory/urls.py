"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url , include
from django.conf.urls.static import static
from django.contrib import admin
from accounts.views import Homepage


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$' ,Homepage.as_view()),
    url(r'^accounts/' ,include('accounts.urls' , namespace='accounts')),
    url(r'^product/' , include('Product.urls',namespace="products")),
    url(r'contacts/',include('Contacts.urls',namespace="contacts")),
    url(r'invoice/',include('invoice.urls',namespace="invoice")),
    url(r'api/',include('accounts.api.urls',namespace="apiviews"))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)