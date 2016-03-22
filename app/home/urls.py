# coding: utf-8

from django.conf.urls import patterns, url

from app.home import views

urlpatterns = patterns(
    '',
    # Display the home page
    url(r'^$', views.index, name='index'),

    # Display the summary page
    url(r'^summary/$', views.Summary.as_view(), name='summary'),
    url(
        r'^summary/('
        r'?P<status>\d+)$',
        views.Summary.as_view(),
        name='summary'
    ),

    #  Connection
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^login/$', 'django.contrib.auth.views.login'),

    # Error page
    url(
        r'^noAccessPermissions$',
        views.noAccessPermissions,
        name='noAccessPermissions'
    ),

    # Get url with Ajax
    url(r'^getUrl/(.+)/(.+)$', views.get_url, name='get_url'),
    url(r'^getUrl/(.+)$', views.get_url, name='get_url'),

    # Carte routiere du centech -iframe
    url(r'^maStartup$', views.maStartup, name='maStartup'),

    # Stock in session the company selected in the main menu
    url(
        r'^setCompanyInSession/(?P<company_id>\d+)$',
        views.setCompanyInSession,
        name='setCompanyInSession'
    ),

    # Form
    url(
        r'^password/$',
        'django.contrib.auth.views.password_change',
        {
            'post_change_redirect': '/company',
            'template_name': 'home/password_update_form.html'
        },
        name="change_password"
    ),
    url(
        r'^accounts/password_change/done/$',
        'django.contrib.auth.views.password_change_done'
    ),
    # url(
    #    r'^password/(?P<pk>\d+)$',
    #    views.PasswordUpdate.as_view(),
    #    name='change_password'
    # ),
)
