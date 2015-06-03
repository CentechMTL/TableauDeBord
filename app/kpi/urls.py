# coding: utf-8

from django.conf.urls import patterns, url,include
from app.kpi.views import trl, irl
from app.kpi import views

urlpatterns = patterns('',
    #Display TRL of the company
    url(r'^trl/(\d+)/$', trl.as_view(), name='trl_filter'),
    #Display IRL of the copmpany
    url(r'^irl/(\d+)/$', irl.as_view(), name='irl_filter'),

    #create
    url(r'irl/add/(\d+)/$', views.IrlCreate.as_view(), name='irl_add'),
    url(r'trl/add/(\d+)/$', views.TrlCreate.as_view(), name='trl_add'),
)