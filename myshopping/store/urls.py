from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^add/$', views.add, name="add"),
    url(r'^list/$', views.list, name="list"),
    url(r'^(?P<s_id>\d+)/update/$', views.update, name="update"),
    url(r'^(?P<s_id>\d+)/detail/$', views.detail, name="detail"),
    url(r'^(?P<s_id>\d+)/(?P<status>\d+)/change_stu/$', views.change_stu, name="change_stu"),
]