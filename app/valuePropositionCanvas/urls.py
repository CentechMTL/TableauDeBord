# coding: utf-8

from django.conf.urls import patterns, url
from app.valuePropositionCanvas import views

urlpatterns = patterns(
    '',

    # Display the canvas of a company
    url(
        r'^(\d+)$',
        views.ValuePropositionCanvasElementList.as_view(),
        name='valuePropositionCanvasElement_list'
    ),

    # Ajax
    url(
        r'^addElement/$',
        views.addElement,
        name='addElement'
    ),
    url(
        r'^getDetail/(?P<element_id>\d+)$',
        views.getDetail,
        name='getDetail'
    ),
    url(
        r'^deleteElement/(?P<element_id>\d+)$',
        views.deleteElement,
        name='deleteElement'
    ),
)
