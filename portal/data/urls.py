from django.conf.urls import url, patterns

urlpatterns = patterns('',
                       url(r'^GetMessages/(?P<id>\d+)/(?P<messageid>\d+)/$', 'data.apis.GetMessages'),
                       url(r'^GetApprovedDisasters/(?P<id>\d+)/(?P<disasterid>\d+)/$',
                           'data.apis.GetApprovedDisasters'),
                       url(r'^GetNotApprovedDisasters/(?P<disasterid>\d+)/$', 'data.apis.GetNotApprovedDisasters'),
                       url(r'^Test/$', 'data.apis.Test'),
                       url(r'^Approval/$', 'data.apis.Approval'),
                       url(r'OrgList/$', 'data.apis.GetOrgList'),
                       url(r'^login/$', 'data.userapis.login', name='login'),
                       url(r'^logout/$', 'data.userapis.logout', name='logout'),
                       url(r'^register/$', 'data.userapis.register', name='register'),
                       url(r'^fill_profile/$', 'data.userapis.fill_profile', name='fill_profile'),

                       )
