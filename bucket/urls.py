from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.items_list, name='items_list'),
    url(r'^item/new/$', views.item_new, name='item_new'),
    url(r'^item/(?P<id>[0-9]+)/edit/$', views.item_edit, name='item_edit'),
    url(r'^item/(?P<id>[0-9]+)/delete/$', views.item_delete, name='item_delete'),
    url(r'^login/$', views.login, name='login'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^logout/$', views.logout, name='logout'),
]