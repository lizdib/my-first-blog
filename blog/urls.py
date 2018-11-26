from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Reply_list, name='post_list'),
    url(r'^$', views.Request_list, name='post_list'),
    url(r'^Reply/(?P<pk>\d+)/$', views.Reply_detail, name='Reply_detail'),
    url(r'^Request/(?P<pk>\d+)/$', views.Request_detail, name='Request_detail'),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
]
