from django.conf.urls import url
from motd.views import *

urlpatterns = [
    # /
    url(r'^$',PostLV.as_view(), name='index'),

    # /post/
    url(r'^$',PostLV.as_view(), name='index'),

    # /post/99/
    url(r'^post/(?P<pk>\d+)/$',PostDV.as_view(), name='post_detail'),

    # /tag/
    url(r'^tag/$',TagTV.as_view(), name='tag_cloud'),

    # /tag/tagname/
    url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),
]