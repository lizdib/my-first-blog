from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Reply_list, name='post_list'),
    url(r'^$', views.Request_list, name='post_list'),
    url(r'^Reply/(?P<pk>\d+)/$', views.Reply_detail, name='Reply_detail'),
    url(r'^Request/(?P<pk>\d+)/$', views.Request_detail, name='Request_detail'),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^show_requests/$', views.Request_list),
    url(r'^show_replies/$', views.Reply_list),
    url(r'^show_request_register/$', views.Request_register),
    url(r'^show_reply_register/$', views.Reply_register),
]
