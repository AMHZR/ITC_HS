from django.conf.urls import patterns, include, url
from django.contrib import admin
from hs_search.views import HSSearchView,HomePageView
from django.conf import settings
from django.conf.urls.static import static

from ajax_select import urls as ajax_select_urls

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^search/$', HSSearchView.as_view(),name='search'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^lookups/', include(ajax_select_urls)),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
