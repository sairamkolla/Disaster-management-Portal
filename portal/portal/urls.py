"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$','authentication.views.login'),
    url(r'^test/$','organisation.views.test'),
    url(r'^best/$','organisation.views.best'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('authentication.urls')),
    url(r'^password_reset/',include('password_reset.urls')),
    url(r'^orgs/', include('organisation.urls')),
    url(r'^siteadmin/',include('siteadmin.urls')),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    ]
