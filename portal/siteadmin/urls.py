from django.conf.urls import url,include,patterns

urlpatterns = patterns('',
        url(r'^$','siteadmin.views.SiteAdminHome'),
        url(r'^make_disaster/$','siteadmin.views.CreateDisaster'),
        url(r'^organisations/$','siteadmin.views.Organisations'),
        url(r'^information/$','siteadmin.views.Information'),
        url(r'^approvals/$','siteadmin.views.Approvals'),
        url(r'^orgsearch/$','siteadmin.views.OrgSearch'),
        url(r'^disastersearch/$','siteadmin.views.DisasterSearch'),
        url(r'^searchtwitter/$','siteadmin.views.SearchTwitter'),

        )

