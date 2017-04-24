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
from django.conf.urls import url , include
from django.contrib import admin
from Product import views as product_views

urlpatterns = [
    url(r'add/$' , product_views.product_add , name='product_add' ),
    url(r'show/$' , product_views.product_show , name='product_show'),
    url(r'show/adjust/$' , product_views.product_show_adjust , name='product_show_adjust'),
    url(r'adjust/(?P<id>\d+)/$' , product_views.product_adjust , name='product_adjust'),
    url(r'detail/(?P<id>\d+)/$' , product_views.product_detail , name='product_detail'),
    url(r'invoice/$' , product_views.invoiceprice , name='product_price'),

]
