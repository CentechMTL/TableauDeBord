# coding: utf-8

from django.conf.urls import patterns, url, include
from app.founder import views

urlpatterns = patterns(
    '',

    # List of founders
    url(
        r'^$',
        views.FounderIndex.as_view(),
        name='index'
    ),
    url(
        r'^(?P<page>\d+)$',
        views.FounderIndex.as_view(),
        name='index'
    ),

    # Detail of a founder
    url(
        r'^detail/(?P<pk>\d+)$',
        views.FounderView.as_view(),
        name='detail'
    ),

    # Forms
    url(
        r'^profile/add$',
        views.FounderCreate.as_view(),
        name='add'
    ),
    url(
        r'^profile/(?P<pk>\d+)$',
        views.FounderUpdate.as_view(),
        name='update'
    ),
)
