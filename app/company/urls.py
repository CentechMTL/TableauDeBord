# coding: utf-8

from django.conf.urls import patterns, url
from app.company import views

urlpatterns = patterns(
    '',
    # List of all companies
    url(
        r'^$',
        views.CompanyIndex.as_view(),
        name='index'
    ),

    # Detail of a company
    url(
        r'^(?P<pk>\d+)/$',
        views.CompanyView.as_view(),
        name='detail'
    ),

    # Form for update the company
    url(
        r'^update/(?P<pk>\d+)$',
        views.CompanyUpdate.as_view(),
        name='update'
    ),

    # Form for add a company
    url(
        r'^add/$',
        views.CompanyCreate.as_view(),
        name='create'
    ),

    url(
        r'^filter$',
        views.filter,
        name='filter'
    ),

    # System of status
    url(
        r'^status/add/$',
        views.CompanyStatusCreate.as_view(),
        name='status_create'
    ),
)
