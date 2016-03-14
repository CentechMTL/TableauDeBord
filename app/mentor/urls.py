# coding: utf-8

from django.conf.urls import patterns, url

from app.mentor import views
from app.mentor.views import MentorView, MentorIndex

urlpatterns = patterns(
    '',

    # List of all mentors
    url(
        r'^$',
        MentorIndex.as_view(),
        name='index'
    ),

    # Display detail of a mentor
    url(
        r'^(?P<pk>\d+)$',
        views.MentorView.as_view(),
        name='detail'
    ),

    # Form
    url(
        r'^profile/add$',
        views.MentorCreate.as_view(),
        name='create'
    ),
    url(
        r'^profile/(?P<pk>\d+)$',
        views.MentorUpdate.as_view(),
        name='update'
    ),
)
