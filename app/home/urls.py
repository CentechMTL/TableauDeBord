# coding: utf-8

from django.conf.urls import patterns, url, include
from app.home import views

urlpatterns = patterns('',
    #Display the home page
    url(r'^$', views.index, name='index'),

    #Display the summary page
    url(r'^summary/$', views.Summary.as_view(), name='summary'),

    #Connection
    url(r'^logout$',views.logout_view,name='logout'),
    url(r'^login/$', 'django.contrib.auth.views.login'),

    #Error page
    url(r'^noAccessPermissions$', views.noAccessPermissions, name='noAccessPermissions'),

    #Get url with Ajax
    url(r'^getUrl/(.+)/(.+)$', views.get_url, name='get_url'),

    #Carte routiere du centech -iframe
    url(r'^maStartup$', views.maStartup, name='maStartup'),

    #Floor plan page
    url(r'^floorPlan$', views.floor_plan.as_view(), name='floorPlan'),

    #Stock in session the company selected in the main menu
    url(r'^setCompanyInSession/(?P<company_id>\d+)$', views.setCompanyInSession, name='setCompanyInSession'),

    #Form
    url(r'^password/(?P<pk>\d+)$', views.PasswordUpdate.as_view(), name='change_password'),
)