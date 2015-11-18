from django.conf.urls import url, patterns

urlpatterns = patterns('',
        url(r'^home/$', 'organisation.views.OrgHome'),
        url(r'^profile/$', 'organisation.views.OrgProfile'),
         url(r'^getuserid/$', 'organisation.views.GetUserId'),
        url(r'^orgsearch/$','organisation.views.orgsearch'),
        )
