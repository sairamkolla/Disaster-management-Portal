from django.conf.urls import url, patterns

urlpatterns = patterns('',
                       url(r'^GetMessages/(?P<id>\d+)/(?P<messageid>\d+)/$', 'data.apis.GetMessages'),
                       url(r'^GetApprovedDisasters/(?P<id>\d+)/(?P<disasterid>\d+)/$',
                           'data.apis.GetApprovedDisasters'),
                       url(r'^GetNotApprovedDisasters/(?P<disasterid>\d+)/$', 'data.apis.GetNotApprovedDisasters'),
                       url(r'^Test/$', 'data.apis.Test'),
                       url(r'^Approval/$', 'data.apis.Approval'),
                       url(r'OrgList/$', 'data.apis.GetOrgList'),

                       )
