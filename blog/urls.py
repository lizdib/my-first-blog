from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Reply_list, name='post_list'),
    url(r'^$', views.Request_list, name='post_list'),
    url(r'^Reply/(?P<pk>\d+)/$', views.Reply_detail, name='Reply_detail'),
    url(r'^Request/(?P<pk>\d+)/$', views.Request_detail, name='Request_detail'),
    url(r'^show_requests/$', views.Request_list),
    url(r'^show_replies/$', views.Reply_list),
    url(r'^show_request_register/$', views.Request_register_list),
    url(r'^show_reply_register/$', views.Reply_register_list),
    url(r'^Reply/new/$', views.Reply_new, name='Reply_new'),
    url(r'^Reply/(?P<pk>\d+)/edit/$', views.Reply_edit, name='Reply_edit'),
    url(r'^Request/new/$', views.Request_new, name='Request_new'),
    url(r'^Request/(?P<pk>\d+)/edit/$', views.Request_edit, name='Request_edit'),
]
