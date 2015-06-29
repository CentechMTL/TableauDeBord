# coding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',

    url(r'^', include('app.home.urls', namespace="home")),
    url(r'^user/', include('app.home.urls', namespace="home")),

    url(r'^company/', include('app.company.urls', namespace="company")),
    url(r'^mentor/', include('app.mentor.urls',namespace="mentor")),
    url(r'^founder/', include('app.founder.urls',namespace="founder")),
    url(r'^kpi/', include('app.kpi.urls', namespace="kpi")),
    url(r'^experiment/', include('app.experiment.urls', namespace="experiment")),
    url(r'^businessCanvas/', include('app.businessCanvas.urls', namespace="businessCanvas")),
    url(r'^finance/', include('app.finance.urls', namespace="finance")),
    url(r'^valuePropositionCanvas/', include('app.valuePropositionCanvas.urls', namespace="valuePropositionCanvas")),
    url(r'^kanboard/', include('app.kanboard.urls', namespace="kanboard")),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()