from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^wish_items/create/$', views.makeawish),
    url(r'^wish_items/1/$', views.wish_item),
    # url(r'^wish_items/(?P<id>\d+)$', views.wish_item),
    url(r'^validate/$', views.validate),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^additem/$', views.additem),



]
