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
from Contacts import views as contact_views

urlpatterns = [
    url(r'add/$' , contact_views.add_contact , name='add_contact' ),
    url(r'allcustomers/$' , contact_views.list_contact_customer , name='all_customers' ),
    url(r'allvendors/$' , contact_views.list_contact_vendor , name='all_vendors' ),
    url(r'detailed/(?P<id>\d+)$' , contact_views.contacts_detail , name='detail_contacts' ),
    url(r'allcustomers/filter/$' , contact_views.list_contact_customer_filter , name='all_customers_filter' )

]
