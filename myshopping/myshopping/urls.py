from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include


urlpatterns = [
    url(r'^', include("commons.urls", namespace="commons")),
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls', namespace="user")),
    url(r'^store/', include('store.urls', namespace="store")),
    url(r'^goods/', include('goods.urls', namespace="goods")),
]
