from django.conf.urls import url,include,patterns

urlpatterns = patterns('',
        url(r'^$','siteadmin.views.admin_home'),
        url(r'^disaster_orgs/$','siteadmin.views.disaster_orgs'),
        url(r'^make_disaster/$','siteadmin.views.create_disaster'),
        url(r'^notify_orgs/(?P<disaster_id>\d+)/$','siteadmin.views.notify_orgs_disaster'),
        )

