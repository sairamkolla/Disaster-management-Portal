from django.conf.urls import url, patterns

urlpatterns = patterns('',
        url(r'^get/(?P<org_id>\d+)/$', 'organisation.views.org_home'),
        url(r'^profile/(?P<org_id>\d+)/$', 'organisation.views.profile'),
        url(r'^create_message/(?P<org_id>\d+)/$', 'organisation.views.create_message_org'), 
        url(r'^view_message/(?P<message_id>\d+)/(?P<org_id>\d+)/$', 'organisation.views.view_message_from_org'), 
        url(r'^view_disaster_org/(?P<disaster_id>\d+)/(?P<org_id>\d+)/$', 'organisation.views.view_disaster_org'), 
        url(r'^decision/(?P<disaster_id>\d+)/(?P<org_id>\d+)/(?P<decision>\d)/$', 'organisation.views.aod'), 
        )
