# coding: utf-8

from django.conf.urls import patterns, url,include
from app.businessCanvas import views

urlpatterns = patterns('',
    #Default page, display the table
    url(r'^(\d+)$', views.BusinessCanvasElementList.as_view(), name='businessCanvasElement_list'),
    #Display the archive
    url(r'^archive/(\d+)$', views.BusinessCanvasElementArchivedList.as_view(), name='businessCanvasElementArchived_list'),

    #Ajax request
    url(r'^addElement/$', views.addElement, name='businessCanvasAddElement'),
    url(r'^getDetail/(?P<element_id>\d+)$', views.getDetail, name='businessCanvasGetDetail'),
    url(r'^deleteElement/(?P<element_id>\d+)$', views.deleteElement, name='businessCanvasDeleteElement'),
    url(r'^deleteArchive/(?P<archive_id>\d+)$', views.deleteArchive, name='businessCanvasDeleteArchive'),
    url(r'^archiver/(?P<company_id>\d+)$', views.archiver, name='businessCanvasArchiver'),
)
