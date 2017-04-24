from django.conf.urls import url , include
from accounts.api import views as accounts_view

urlpatterns = [
    url(r'listview/$' , accounts_view.Postlistapiview.as_view() , name='list' ),
    url(r'^detail/(?P<id>\d+)/$', accounts_view.Postdetailapiview.as_view() , name="retrive"),
    url(r'^update/(?P<id>\d+)/$', accounts_view.Postupdateapiview.as_view() , name="update")

]
