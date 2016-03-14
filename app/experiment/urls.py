# coding: utf-8

from django.conf.urls import patterns, url, include
from app.experiment import views

urlpatterns = patterns(
    '',

    # Display all experiment of a company
    url(
        r'^(\d+)$',
        views.CustomerExperimentList.as_view(),
        name='experiment_list'
    ),

    # Create, update, delete
    url(
        r'add/(\d+)/$',
        views.CustomerExperimentCreate.as_view(),
        name='experiment_add'
    ),
    url(
        r'update/(?P<pk>\d+)/$',
        views.CustomerExperimentUpdate.as_view(),
        name='experiment_update'
    ),
    url(
        r'delete/(?P<pk>\d+)/$',
        views.CustomerExperimentDelete.as_view(),
        name='experiment_delete'
    ),
)
