from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from foof.views import MoofDetailView

urlpatterns = patterns('',
    url(r'^$', MoofDetailView.as_view()),
    url(r"^search/", include("watson.urls", namespace="watson"))
)

if settings.SHOW_ADMIN:
    urlpatterns += (url(r'^admin/', include(admin.site.urls)),
)