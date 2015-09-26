from django.conf.urls import urls

urlpatterns = ['',
        url(r'login/$','views.login'),
        url(r'auth/$','views.auth_view'),
        url(r'logout/$','views.logout'),
        url(r'loggedin/$','views.loggedin'),
        url(r'invalid/$','views.invalid_login'),
]
