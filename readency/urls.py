from django.conf.urls import patterns, include, url
from django.contrib import admin
from rdcy_auth.views import PocketAuthenticationView, LoginView, LogoutView
from rdcy_platform.views import ProfileView, ServiceConnectionView
from rdcy_admin.views import ServiceCreateView, ProfileListView
from rdcy_api.readency_api.views import ServiceConnectionCreateApi


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'readency.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth/pocket/$', PocketAuthenticationView.as_view(), name="pocket"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^service/create/$', ServiceCreateView.as_view(), name="service_create"),

    # ---------------------------------------------------------
    #  Service Connections 
    # ---------------------------------------------------------
    url(r'^connections/$', ServiceConnectionView.as_view(), name="connections_list"),

    # ---------------------------------------------------------
    #  Profiles
    # ---------------------------------------------------------
    url(r'^profile/$', ProfileView.as_view(), name="profile"),

    #----------------------------------------------------------
    #  Social Authentication
    # ---------------------------------------------------------

    url('', include('social.apps.django_app.urls', namespace='social')),

    #----------------------------------------------------------
    #  API endpoints
    # ---------------------------------------------------------
    url(r'^api/connection/create/$', ServiceConnectionCreateApi.as_view(), name="api_connection_create"),

    # ---------------------------------------------------------
    #  Other
    # ---------------------------------------------------------
    url(r'^$', ProfileView.as_view(), name="profile"),

)
