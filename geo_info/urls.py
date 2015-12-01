from django.conf.urls import url
from geo_info import views

urlpatterns = [
    url(r'^$', views.country_by_ip, name='take_info'),
    url(r'^all/$', views.GeoInfoView.as_view(), name='geo_info'),
    url(r'^delete/$', views.delete_data, name='delete_data'),
]
