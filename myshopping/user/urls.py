from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r"^check_name/$", views.check_name, name='check_name'),
    url(r"^check_nickname/$", views.check_nickname, name='check_nickname'),
    url(r"^user_info/$", views.user_info, name='user_info'),
    url(r"^(?P<u_id>\d+)/changepwd/$", views.changepwd, name='changepwd'),
    url(r"^checkpwd/$", views.checkpwd, name='checkpwd'),
]
