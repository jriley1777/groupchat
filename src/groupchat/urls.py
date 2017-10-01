from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^friend/list$', views.list_friends, name='list_friends'),
    url(r'^room/list$', views.list_rooms, name='list_rooms'),
    url(r'^room/(?P<room_id>[0-9]+)/get_messages/$', views.get_room_messages, name='get_room_messages'),
    url(r'^room/(?P<room_id>[0-9]+)/message/add$', views.add_room_message, name='add_room_message'),
]
urlpatterns += staticfiles_urlpatterns()