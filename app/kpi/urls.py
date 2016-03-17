# coding: utf-8

from django.conf.urls import patterns, url, include
from app.kpi.views import trl, irl
from app.kpi import views

urlpatterns = patterns(
    '',

    # Display TRL of the company
    url(
        r'^trl/(\d+)/$',
        trl.as_view(),
        name='trl_filter'
    ),

    # Display IRL of the copmpany
    url(
        r'^irl/(\d+)/$',
        irl.as_view(),
        name='irl_filter'
    ),

    # create
    url(
        r'irl/add/(\d+)/$',
        views.IrlCreate.as_view(),
        name='irl_add'
    ),
    url(
        r'trl/add/(\d+)/$',
        views.TrlCreate.as_view(),
        name='trl_add'
    ),

    # update
    url(
        r'irl/update/(?P<pk>\d+)/$',
        views.IrlUpdate.as_view(),
        name='irl_update'
    ),
    url(
        r'trl/update/(?P<pk>\d+)/$',
        views.TrlUpdate.as_view(),
        name='trl_update'
    ),

    # delete
    url(
        r'irl/delete/(?P<pk>\d+)/$',
        views.IrlDelete.as_view(),
        name='irl_delete'
    ),
    url(
        r'trl/delete/(?P<pk>\d+)/$',
        views.TrlDelete.as_view(),
        name='trl_delete'
    ),
)
