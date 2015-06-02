from django.conf.urls import patterns, url, include
from app.home import views

urlpatterns = patterns('',
    #Display the home page
    url(r'^$', views.index, name='index'),

    #Connection
    url(r'^logout$',views.logout_view,name='logout'),
    url(r'^login/$', 'django.contrib.auth.views.login'),

    #Error page
    url(r'^noAccessPermissions$', views.noAccessPermissions, name='noAccessPermissions'),

    #Stock in session the company selected in the main menu
    url(r'^setCompanyInSession/(?P<company_id>\d+)$', views.setCompanyInSession, name='setCompanyInSession'),

    #Form
    url(r'^password/(?P<pk>\d+)$', views.PasswordUpdate.as_view(), name='change_password'),
)