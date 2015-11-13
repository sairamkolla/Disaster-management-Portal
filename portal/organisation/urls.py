from django.conf.urls import url, patterns

urlpatterns = patterns('',
        #url(r'^get/(?P<org_id>\d+)/$', 'organisation.views.org_home'),
        url(r'^home/$', 'organisation.views.org_home'),
        #url(r'^profile/(?P<org_id>\d+)/$', 'organisation.views.profile'),
        url(r'^profile/$', 'organisation.views.profile'),
        #url(r'^create_message/(?P<org_id>\d+)/$', 'organisation.views.create_message_org'), 
        url(r'^create_message/$', 'organisation.views.create_message_org'),
         url(r'^getuserid/$', 'organisation.views.getuserid'),
        )
