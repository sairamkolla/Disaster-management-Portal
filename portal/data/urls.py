from django.conf.urls import url, patterns

urlpatterns = patterns('',
        url(r'^getmessages/(?P<id>\d+)/(?P<messageid>\d+)/$', 'data.views.getmessages'),
        url(r'^getapproveddisasters/(?P<id>\d+)/(?P<disasterid>\d+)/$', 'data.views.getapproveddisasters'),
        url(r'^getnotapproveddisasters/(?P<disasterid>\d+)/$', 'data.views.getnotapproveddisasters'),
         url(r'^test/$', 'data.views.test'),


        )
