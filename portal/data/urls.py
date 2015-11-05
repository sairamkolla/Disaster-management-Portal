from django.conf.urls import url, patterns

urlpatterns = patterns('',
        url(r'^getmessages/(?P<id>\d+)/(?P<messageid>\d+)/$', 'data.views.getmessages'),
        url(r'^getdisasters/(?P<id>\d+)/(?P<disasterid>\d+)/$', 'data.views.getdisasters'),
        url(r'^getuserid/$', 'data.views.getuserid'),
        )
